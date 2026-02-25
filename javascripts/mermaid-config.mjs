import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs"

mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    theme: "base",
    flowchart: {
        htmlLabels: true,
        useMaxWidth: true,
        curve: "basis"
    }
})

window.mermaid = mermaid
