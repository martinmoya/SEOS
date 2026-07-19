## Sprint 14 - Technical Log
Architecture Decisions (ADRs)

ADR-028: Cross-Language Integration. SEOS Python backend communicates with the VS Code TypeScript frontend via standard HTTP REST API, ensuring language agnosticism.

ADR-029: IDE Context Menus. The extension hooks into editor/context menus to provide seamless "right-click -> explain" functionality without leaving the coding flow.

## Files Created
vscode-extension/package.json
vscode-extension/tsconfig.json
vscode-extension/src/extension.ts
vscode-extension/.vscode/launch.json

## Dependencies Added
axios (for HTTP requests in TS)
typescript, @types/vscode, @types/node (dev dependencies)
