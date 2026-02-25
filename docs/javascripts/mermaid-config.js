/**
 * Configurazione Mermaid per Material for MkDocs (supporto nativo)
 * Material legge window.mermaidConfig prima di inizializzare Mermaid.
 * securityLevel 'loose' è necessario per i tag HTML nei nodi (es. <br/>)
 */
window.mermaidConfig = {
    startOnLoad: false,
    theme: 'base',
    securityLevel: 'loose',
    flowchart: {
        htmlLabels: true,
        useMaxWidth: true,
        curve: 'basis'
    }
};
