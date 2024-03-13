import * as vscode from 'vscode';
import * as net from 'net';

let socket: net.Socket | undefined;
let disposable: vscode.Disposable | undefined;

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	socket = new net.Socket();
	socket.connect(12345, 'localhost' , () => {
		console.log('Connected to the server!');
	});

	socket.on('error', (err) => {
		console.error(err);
	});

	disposable = vscode.window.onDidChangeTextEditorSelection((event) => {
		const editor = vscode.window.activeTextEditor;
		if (editor) {
			const position = editor.selection.active;
			const currentLine = editor.document.lineAt(position.line);
			const currentLineText = currentLine.text;

			if (socket) {
				socket.write(currentLineText + '\n');
				console.log('Sent: ' + currentLineText);
			}
		}
	});

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "braille-reader" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {
	if (disposable) {
		disposable.dispose();
	}

	if (socket) {
		socket.end();
	}
}
