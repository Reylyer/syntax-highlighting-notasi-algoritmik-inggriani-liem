"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const vscode = require("vscode");
const tokenTypes = new Map();
const tokenModifiers = new Map();
const legend = (function () {
    const tokenTypesLegend = [
        'comment', 'string', 'keyword', 'number', 'regexp', 'operator', 'namespace',
        'type', 'struct', 'class', 'interface', 'enum', 'typeParameter', 'function',
        'method', 'decorator', 'macro', 'variable', 'parameter', 'property', 'label'
    ];
    tokenTypesLegend.forEach((tokenType, index) => tokenTypes.set(tokenType, index));
    const tokenModifiersLegend = [
        'declaration', 'documentation', 'readonly', 'static', 'abstract', 'deprecated',
        'modification', 'async'
    ];
    tokenModifiersLegend.forEach((tokenModifier, index) => tokenModifiers.set(tokenModifier, index));
    return new vscode.SemanticTokensLegend(tokenTypesLegend, tokenModifiersLegend);
})();
function activate(context) {
    context.subscriptions.push(vscode.languages.registerDocumentSemanticTokensProvider({ language: 'algoritmik', scheme: 'file' }, new DocumentSemanticTokensProvider(), legend));
}