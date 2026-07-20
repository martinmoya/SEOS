"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = require("vscode");
const axios_1 = require("axios");
const SEOS_API_URL = 'http://127.0.0.1:8080/chat';
function activate(context) {
    console.log('SEOS Extension is now active!');
    let disposable = vscode.commands.registerCommand('seos.explainCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage('No active editor!');
            return;
        }
        const selection = editor.selection;
        const selectedText = editor.document.getText(selection);
        if (!selectedText) {
            vscode.window.showWarningMessage('Please select some code first.');
            return;
        }
        const prompt = `Explain the following code concisely:\n\n${selectedText}`;
        try {
            await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: "Asking SEOS...",
                cancellable: false
            }, async () => {
                const response = await axios_1.default.post(SEOS_API_URL, { message: prompt });
                const explanation = response.data.response;
                // Mostrar la respuesta en un panel de salida
                const outputChannel = vscode.window.createOutputChannel('SEOS');
                outputChannel.show(true);
                outputChannel.appendLine('--- SEOS EXPLANATION ---');
                outputChannel.appendLine(explanation);
                outputChannel.appendLine('------------------------');
            });
        }
        catch (error) {
            vscode.window.showErrorMessage(`SEOS API Error: ${error.message}. Is SEOS running (/serve)?`);
        }
    });
    context.subscriptions.push(disposable);
}
function deactivate() { }
//# sourceMappingURL=extension.js.map