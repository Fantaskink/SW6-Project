import * as vscode from 'vscode';
import * as net from 'net';

let socket: net.Socket | undefined;
let disposable: vscode.Disposable | undefined;
let reconnectInterval: NodeJS.Timeout | undefined;

const connectToServer = () => {
    // If already connected, do nothing
    if (socket && socket.connecting) {
        return;
    }

    socket = new net.Socket();

    socket.connect(12345, 'localhost', () => {
        console.log('Connected to the server!');
        if (reconnectInterval) {
            clearInterval(reconnectInterval);
            reconnectInterval = undefined;
        }
    });

    socket.on('error', (err) => {
        console.error(err);
        // If not already trying to reconnect, start trying
        if (!reconnectInterval) {
            reconnectInterval = setInterval(connectToServer, 5000); // Retry every 5 seconds
        }
    });

    socket.on('close', () => {
        console.log('Disconnected from the server');
        // If not already trying to reconnect, start trying
        if (!reconnectInterval) {
            reconnectInterval = setInterval(connectToServer, 5000); // Retry every 5 seconds
        }
    });
};

export function activate(context: vscode.ExtensionContext) {
    connectToServer();

    disposable = vscode.window.onDidChangeTextEditorSelection((event) => {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const position = editor.selection.active;
            const currentLine = editor.document.lineAt(position.line);
            const currentLineText = currentLine.text;

            if (socket && !socket.connecting) {
                socket.write(currentLineText);
                console.log('Sent:', currentLineText);
            }
        }
    });

    console.log('Congratulations, your extension "braille-reader" is now active!');

    context.subscriptions.push(disposable);
}

export function deactivate() {
    if (disposable) {
        disposable.dispose();
    }

    if (socket) {
        socket.end();
    }

    if (reconnectInterval) {
        clearInterval(reconnectInterval);
    }
}