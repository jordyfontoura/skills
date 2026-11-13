// Somente nos testes: ativa o fluxo interativo com streams controláveis por pipes.
// Não emula renderização, tamanho real de terminal ou comportamento do shell.
Object.defineProperty(process.stdin, 'isTTY', { value: true });
Object.defineProperty(process.stdout, 'isTTY', { value: true });
Object.defineProperty(process.stdout, 'columns', { value: 100 });
process.stdin.setRawMode = () => process.stdin;
