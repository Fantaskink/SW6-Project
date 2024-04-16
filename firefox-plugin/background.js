const socket = new WebSocket('ws://localhost:12345');

browser.menus.create({
  id: "braille-ocr",
  title: "Send image to OCR server",
  contexts: ["image"]
});
 
browser.menus.onClicked.addListener(async function (info, tab) {
  if (info.menuItemId == "braille-ocr") {
    console.log(info.srcUrl);
    const response = await fetch(info.srcUrl);
    const blob = await response.blob();

    // Convert the image to a Base64 string
    const reader = new FileReader();
    reader.onloadend = function() {
      const base64data = reader.result;

      // Send the image over the socket
      socket.send(base64data);
    }
    reader.readAsDataURL(blob);
  }
});