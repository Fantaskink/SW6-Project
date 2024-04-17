browser.menus.create({
  id: "braille-ocr",
  title: "Send image to OCR server",
  contexts: ["image"]
});

let socket;

function connect() {
  socket = new WebSocket('ws://localhost:12347');

  socket.onerror = function(event) {
    console.error("WebSocket error observed:", event);
  };

  socket.onopen = function(event) {
    console.log("WebSocket connection opened");
  };

  socket.onclose = function(event) {
    console.log("WebSocket connection closed");
    // Attempt to reconnect after 5 seconds
    setTimeout(connect, 5000);
  };
}

connect();
 
browser.menus.onClicked.addListener(async function (info, tab) {
  if (info.menuItemId == "braille-ocr") {
    console.log("Sending image to OCR server");
    const response = await fetch(info.srcUrl);
    const blob = await response.blob();

    // Convert the image to a Base64 string
    const reader = new FileReader();
    reader.onloadend = function() {
      const base64data = reader.result;

      // Create a JSON object with the image data and an indicator
      const data = JSON.stringify({
        type: 'image',
        content: base64data
      });

      // Send the image over the socket
      socket.send(data);
    }
    reader.readAsDataURL(blob);
  }
});