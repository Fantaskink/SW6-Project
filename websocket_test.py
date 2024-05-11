import asyncio
import websockets
from PIL import Image
import io
import base64
import json
import pytesseract
import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)


def connect_socket():
    global sock
    while True:
        try:
            # Close the socket if it's already open
            if sock:
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(server_address)
            # If the connection is successful, break the loop
            break
        except Exception as e:
            print(f"Error: {e}. Trying to reconnect in 5 seconds.")
            time.sleep(5)


connect_socket()


async def echo(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        if data['type'] == 'image':
            await ocr_image(data['content'])


async def ocr_image(data_url):
    # Split the 'data:image/jpeg;base64,' part from the actual image data
    mime, base64_string = data_url.split(',')

    base64_bytes = base64.b64decode(base64_string)
    image_bytes = io.BytesIO(base64_bytes)
    image = Image.open(image_bytes)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    print(text)
    # Send the text to the server
    while True:
        try:
            sock.sendall(text.encode('utf-8'))
            # If the data is sent successfully, break the loop
            break
        except Exception as e:
            print(f"Error: {e}. Trying to reconnect in 5 seconds.")
            connect_socket()


async def main():
    server = await websockets.serve(echo, 'localhost', 12347)
    await server.wait_closed()


asyncio.run(main())
