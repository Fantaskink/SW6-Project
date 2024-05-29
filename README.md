# SW6-Project
 
# Setup

# Generating the required ANTLR files

1. Install the ANTLR v4 plugin in Pycharm or another JetBrains IDE.
2. Right click "uncontracted_braille.g4" in the ANTLR4 folder and select "Configure ANTLR".
3. In Language, write "Python3" and click "OK".
4. Right click the grammar file again and choose "Generate ANTLR Recognizer".
5. Repeat the same steps for the other grammar files.


# Running the main program
1. Install the required packages with pip.
2. Run "main.py" to launch the GUI.
3. Run "firefox_server.py" to launch the firefox image OCR server
   

# Running the VSCode plugin
1. In VSCode, open the "braille-reader" directory.
2. Open extension.ts.
3. Press F5 to debug the extension.
4. Once it successfully connects to the display software, open a file in the newly opened window.
5. Place the cursor on any line of text or code.
6. The display software will receive, translate and display the selected line of code.

# Running the Firefox extension
1. Open the following URL: "about:debugging#/runtime/this-firefox".
2. Press "Load Temporary Add-On".
3. Select "manifest.json" within the "firefox-plugin" directory.
4. Right click an image and select "Send image to OCR server"
5. The text on the image will be extracted, sent to the braille display server, translated and rendered
