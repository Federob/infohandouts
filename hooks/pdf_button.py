"""
Hook MkDocs per aggiungere bottone download PDF
Aggiunge un bottone in alto a destra di ogni pagina
"""

import os
from pathlib import Path


def _build_pdf_url(page, pdf_name: str) -> str:
    """
    Rende l'URL del PDF relativo alla pagina corrente, così funziona
    anche quando il sito è pubblicato in una sottocartella (es. GitHub Pages).
    """
    page_url = (page.url or "").lstrip('/')
    if page_url.endswith('index.html'):
        page_url = page_url[: -len('index.html')]
    page_url = page_url.rstrip('/')

    depth = len([p for p in page_url.split('/') if p])
    rel_prefix = '../' * depth
    return f"{rel_prefix}pdf/{pdf_name}"


def on_page_content(html, page, config, files):
    """
    Hook chiamato dopo che il contenuto della pagina è stato convertito in HTML
    Aggiunge un bottone per scaricare il PDF della pagina corrente
    """

    # Calcola il nome del PDF basato sul file sorgente
    source_path = page.file.src_path  # es: "algocoding/01_flowgorithm.md"
    pdf_name = source_path.replace('/', '_').replace('.md', '.pdf')
    pdf_url = _build_pdf_url(page, pdf_name)

    # Verifica se il PDF esiste (durante build potrebbe non esistere ancora)
    # Questa è una semplice verifica, il PDF verrà generato dopo
    pdf_exists = True  # Assumiamo che verrà generato

    if not pdf_exists:
        return html

    # HTML del bottone download PDF
    pdf_button = f'''
<div style="position: relative; float: right; margin: 0 0 20px 20px;">
    <a href="{pdf_url}"
       download
       class="md-button md-button--primary"
       title="Scarica questa pagina in formato PDF"
       style="
           background-color: #2196F3;
           color: white;
           padding: 10px 20px;
           border-radius: 4px;
           text-decoration: none;
           display: inline-flex;
           align-items: center;
           gap: 8px;
           font-weight: 500;
           box-shadow: 0 2px 4px rgba(0,0,0,0.2);
           transition: all 0.3s ease;
       "
       onmouseover="this.style.backgroundColor='#1976D2'; this.style.boxShadow='0 4px 8px rgba(0,0,0,0.3)';"
       onmouseout="this.style.backgroundColor='#2196F3'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.2)';">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" y1="15" x2="12" y2="3"></line>
        </svg>
        Scarica PDF
    </a>
</div>
<div style="clear: both;"></div>
'''

    # Inserisci il bottone all'inizio del contenuto
    html = pdf_button + html

    return html
