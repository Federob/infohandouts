#!/usr/bin/env python3
"""
Script per generare PDF da file Markdown con supporto Mermaid
Utilizzato durante il build di MkDocs per creare PDF scaricabili
"""

import os
import sys
import subprocess
import tempfile
import json
import functools
from pathlib import Path
from typing import List, Dict
import http.server
import socketserver
import threading
import time

# Configurazione
DOCS_DIR = Path("docs")
PDF_OUTPUT_DIR = Path("docs/pdf")
PORT = 8765


def get_markdown_files() -> List[Path]:
    """Trova tutti i file markdown nella directory docs/"""
    markdown_files = []
    docs_abs = Path.cwd() / DOCS_DIR

    for root, dirs, files in os.walk(docs_abs):
        # Escludi directory che iniziano con punto
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                abs_path = Path(root) / file
                markdown_files.append(abs_path)

    return markdown_files


def create_html_with_mermaid(md_file: Path, output_html: Path) -> None:
    """Crea un file HTML dal markdown con supporto Mermaid renderizzato"""

    # Leggi il markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Template HTML con Mermaid support
    html_template = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/marked@11.1.1/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <style>
        @page {{
            size: A4;
            margin: 20mm;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            font-size: 11pt;
            max-width: 100%;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            page-break-before: always;
            margin-top: 0;
        }}
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 25px;
            page-break-after: avoid;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
            page-break-after: avoid;
        }}
        h4 {{
            color: #666;
            page-break-after: avoid;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            page-break-inside: avoid;
            font-size: 0.9em;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 15px;
            color: #555;
            font-style: italic;
            margin: 15px 0;
        }}
        .mermaid {{
            page-break-inside: avoid;
            margin: 20px auto;
            text-align: center;
            background-color: white;
        }}
        .mermaid svg {{
            max-width: 100%;
            height: auto;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 25px 0;
        }}
        #content {{
            opacity: 0;
            transition: opacity 0.3s;
        }}
        #content.ready {{
            opacity: 1;
        }}
    </style>
</head>
<body>
    <div id="content"></div>
    <script>
        const markdownContent = `{markdown_content}`;

        // Initialize mermaid
        mermaid.initialize({{
            startOnLoad: false,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {{
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis'
            }}
        }});

        async function renderContent() {{
            // Store mermaid blocks
            const mermaidBlocks = [];
            const textWithPlaceholders = markdownContent.replace(/```mermaid\\n([\\s\\S]*?)```/g, (match, code) => {{
                const id = mermaidBlocks.length;
                mermaidBlocks.push(code.trim());
                return `<div class="mermaid" id="mermaid-${{id}}">%%%PLACEHOLDER_${{id}}%%%</div>`;
            }});

            // Convert markdown to HTML
            const html = marked.parse(textWithPlaceholders);
            document.getElementById('content').innerHTML = html;

            // Render mermaid diagrams
            for (let i = 0; i < mermaidBlocks.length; i++) {{
                const element = document.getElementById(`mermaid-${{i}}`);
                if (element) {{
                    try {{
                        const {{ svg }} = await mermaid.render(`mermaid-svg-${{i}}`, mermaidBlocks[i]);
                        element.innerHTML = svg;
                    }} catch (error) {{
                        console.error(`Error rendering mermaid diagram ${{i}}:`, error);
                        element.innerHTML = `<pre>${{mermaidBlocks[i]}}</pre>`;
                    }}
                }}
            }}

            // Mark content as ready
            document.getElementById('content').classList.add('ready');
            window.renderComplete = true;
            console.log('Rendering complete');
        }}

        renderContent();
    </script>
</body>
</html>'''

    # Estrai il titolo dal primo heading
    title = "Documento"
    for line in md_content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break

    # Escape backticks nel markdown per JavaScript
    md_escaped = md_content.replace('`', '\\`').replace('${', '\\${')

    # Crea HTML
    html_content = html_template.format(
        title=title,
        markdown_content=md_escaped
    )

    # Scrivi il file HTML
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)


def start_http_server(directory: Path, port: int) -> threading.Thread:
    """Avvia un server HTTP in background"""
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(directory)
    )
    httpd = socketserver.TCPServer(("", port), handler)

    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    return server_thread


def generate_pdf_from_html(html_path: Path, pdf_path: Path, port: int) -> bool:
    """Genera PDF da HTML usando Chrome headless"""

    # Percorso relativo per l'URL
    rel_path = html_path.name
    url = f"http://localhost:{port}/{rel_path}"

    # Comando Chrome headless
    chrome_commands = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    ]

    chrome_path = None
    for cmd in chrome_commands:
        try:
            result = subprocess.run(['which', cmd], capture_output=True, text=True)
            if result.returncode == 0:
                chrome_path = cmd
                break
        except:
            # Try to use the path directly
            if os.path.exists(cmd):
                chrome_path = cmd
                break

    if not chrome_path:
        print("❌ Chrome/Chromium non trovato. Installalo per generare PDF.")
        return False

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--virtual-time-budget=15000",
        "--run-all-compositor-stages-before-draw",
        "--no-margins",
        url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0 and pdf_path.exists():
            return True
        else:
            print(f"❌ Errore generazione PDF: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("❌ Timeout durante generazione PDF")
        return False
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False


def main():
    """Funzione principale"""
    # Assicurati di essere nella directory root del progetto
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)

    print("🚀 Inizio generazione PDF dai file Markdown...")
    print(f"📁 Directory di lavoro: {os.getcwd()}")

    # Crea directory output se non esiste
    PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Trova tutti i file markdown
    md_files = get_markdown_files()
    print(f"📄 Trovati {len(md_files)} file markdown")

    if not md_files:
        print("⚠️  Nessun file markdown trovato")
        return
    docs_abs = project_root / DOCS_DIR

    # Crea directory temporanea per HTML
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Avvia server HTTP
        print(f"🌐 Avvio server HTTP su porta {PORT}...")
        server_thread = start_http_server(temp_path, PORT)
        time.sleep(2)  # Aspetta che il server si avvii

        successful = 0
        failed = 0

        for md_file in md_files:
            # Calcola percorso relativo rispetto a docs/
            rel_path = md_file.relative_to(docs_abs)

            # Percorso output PDF
            pdf_name = str(rel_path).replace('/', '_').replace('.md', '.pdf')
            pdf_path = PDF_OUTPUT_DIR / pdf_name

            print(f"\n📝 Processando: {rel_path}")

            # Crea HTML temporaneo
            html_path = temp_path / f"{pdf_name}.html"
            create_html_with_mermaid(md_file, html_path)

            # Genera PDF
            if generate_pdf_from_html(html_path, pdf_path, PORT):
                print(f"   ✅ PDF generato: {pdf_path}")
                successful += 1
            else:
                print(f"   ❌ Fallito: {pdf_path}")
                failed += 1

        print(f"\n{'='*50}")
        print(f"✅ PDF generati con successo: {successful}")
        if failed > 0:
            print(f"❌ PDF falliti: {failed}")
            # Fallisce lo script per evidenziare l'errore nel CI
            sys.exit(1)
        print(f"{'='*50}")


if __name__ == "__main__":
    main()
