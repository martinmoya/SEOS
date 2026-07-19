"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const axios_1 = __importDefault(require("axios"));
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