/**
 * Configurazione Mermaid per supportare <br/> nei nodi
 * Questo script forza Mermaid a usare htmlLabels per supportare HTML nei testi
 */

// Configura PRIMA che il DOM sia caricato
if (typeof window !== 'undefined') {
    window.mermaidConfig = {
        startOnLoad: false,
        theme: 'base',
        securityLevel: 'loose',
        flowchart: {
            htmlLabels: true,
            useMaxWidth: true,
            curve: 'basis'
        },
        themeVariables: {
            // Lascia che il CSS gestisca i colori
        }
    };
}

document.addEventListener('DOMContentLoaded', function() {
    // Aspetta che Mermaid sia caricato dal plugin mkdocs-mermaid2
    if (typeof mermaid !== 'undefined') {
        // Configurazione Mermaid per supportare HTML labels (incluso <br/>)
        mermaid.initialize({
            startOnLoad: true,
            theme: 'base',
            securityLevel: 'loose',
            flowchart: {
                htmlLabels: true,
                useMaxWidth: true,
                curve: 'basis'
            },
            themeVariables: {
                // Lascia che il CSS gestisca i colori
            }
        });

        console.log('Mermaid configurato con supporto htmlLabels');

        // Re-render di tutti i diagrammi esistenti
        const diagrams = document.querySelectorAll('.mermaid');
        diagrams.forEach((diagram, index) => {
            const id = `mermaid-${index}`;
            const content = diagram.textContent;
            mermaid.render(id, content).then(result => {
                diagram.innerHTML = result.svg;
            });
        });
    }
});
