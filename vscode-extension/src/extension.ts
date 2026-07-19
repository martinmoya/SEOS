import * as vscode from 'vscode';
import axios from 'axios';

const SEOS_API_URL = 'http://127.0.0.1:8080/chat';

export function activate(context: vscode.ExtensionContext) {
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
                const response = await axios.post(SEOS_API_URL, { message: prompt });
                const explanation = response.data.response;
                
                // Mostrar la respuesta en un panel de salida
                const outputChannel = vscode.window.createOutputChannel('SEOS');
                outputChannel.show(true);
                outputChannel.appendLine('--- SEOS EXPLANATION ---');
                outputChannel.appendLine(explanation);
                outputChannel.appendLine('------------------------');
            });
        } catch (error: any) {
            vscode.window.showErrorMessage(`SEOS API Error: ${error.message}. Is SEOS running (/serve)?`);
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
