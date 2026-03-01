#!/usr/bin/env python3
"""
Converte i file Markdown MkDocs Material in formato Quarto (.qmd).
Gestisce: admonition, mermaid, pyodide, front matter, link interni, video.
"""

import os
import re
from pathlib import Path

DOCS_DIR = Path("/home/user/infohandouts/docs")

# Mapping tipi admonition MkDocs → Quarto callout
TYPE_MAP = {
    "note": "note",
    "abstract": "note",
    "info": "note",
    "tip": "tip",
    "hint": "tip",
    "important": "important",
    "success": "tip",
    "question": "note",
    "warning": "warning",
    "caution": "caution",
    "danger": "important",
    "error": "important",
    "bug": "important",
    "example": "note",
    "quote": "note",
    "cite": "note",
}

# Blocco di setup per input() in Pyodide
INPUT_SETUP_BLOCK = '''```{pyodide-python}
#| autorun: true
#| output: false
#| echo: false
import js

def _browser_input(prompt=""):
    result = js.prompt(str(prompt))
    if result is None:
        raise EOFError("Input annullato")
    return result

__builtins__.input = _browser_input
```

'''


def convert_admonitions(content: str) -> str:
    """Converte !!! type 'title' / ??? type 'title' in ::: {.callout-type}."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Match inizio admonition: !!! type "title" oppure ??? / ???+
        match = re.match(
            r'^(\?{3}\+?|!{3})\s+(\w+)\s*(?:"([^"]*)")?\s*$', line
        )

        if match:
            prefix = match.group(1)
            adm_type = match.group(2).lower()
            title = match.group(3) or ""

            quarto_type = TYPE_MAP.get(adm_type, "note")

            # Collapsible?
            attrs = f".callout-{quarto_type}"
            if prefix.startswith("???"):
                if prefix == "???+":
                    attrs += ' collapse="false"'
                else:
                    attrs += ' collapse="true"'

            result.append(f"::: {{{attrs}}}")
            if title:
                result.append(f"## {title}")

            i += 1

            # Salta eventuale riga vuota dopo !!!
            if i < len(lines) and lines[i].strip() == "":
                i += 1

            # Raccogli contenuto indentato (4 spazi o 1 tab)
            while i < len(lines):
                if lines[i] == "":
                    # Riga vuota: controlla se il contenuto continua dopo
                    j = i + 1
                    while j < len(lines) and lines[j] == "":
                        j += 1
                    if j < len(lines) and (
                        lines[j].startswith("    ") or lines[j].startswith("\t")
                    ):
                        result.append("")
                        i += 1
                    else:
                        break
                elif lines[i].startswith("    "):
                    result.append(lines[i][4:])
                    i += 1
                elif lines[i].startswith("\t"):
                    result.append(lines[i][1:])
                    i += 1
                else:
                    break

            result.append(":::")
            result.append("")
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def convert_mermaid_fences(content: str) -> str:
    """Converte ```mermaid in ```{mermaid}."""
    return re.sub(r"```mermaid\s*\n", "```{mermaid}\n", content)


def convert_pyodide_fences(content: str) -> str:
    """Converte ```pyodide in ```{pyodide-python}."""
    return re.sub(r"```pyodide\s*\n", "```{pyodide-python}\n", content)


def convert_front_matter(content: str) -> str:
    """Converte front matter MkDocs in formato Quarto."""
    # Gestisci hide: [navigation, toc, footer]
    content = re.sub(
        r"---\s*\nhide:\s*\n(?:\s*-\s*(?:navigation|toc|footer)\s*\n)+---",
        "---\ntoc: false\npage-navigation: false\n---",
        content,
    )
    return content


def convert_internal_links(content: str) -> str:
    """Converte link interni da .md a .qmd."""
    # [text](path.md) → [text](path.qmd)
    content = re.sub(r"\]\(([^)]*?)\.md\)", r"]\(\1.qmd)", content)
    # [text](path/to/file/) → [text](path/to/file.qmd) (MkDocs pretty URLs)
    content = re.sub(
        r'\]\((\./)?([a-zA-Z0-9_/]+)/\)',
        lambda m: f']({m.group(1) or ""}{m.group(2)}.qmd)',
        content,
    )
    return content


def convert_video_embeds(content: str) -> str:
    """Converte embed video mkdocs-video in shortcode Quarto."""
    # ![type:video](path.mp4) → {{< video path.mp4 >}}
    content = re.sub(
        r"!\[(?:type:video)?\]\(([^)]+\.mp4)\)",
        r"{{< video \1 >}}",
        content,
    )
    return content


def convert_mkdocs_buttons(content: str) -> str:
    """Converte i bottoni MkDocs Material in link Quarto con stile."""
    # [text](url){.md-button .md-button--primary} non è supportato in Quarto
    # Lasciamo i link con class come HTML inline dove necessario
    # Per ora non convertiamo - Quarto non ha equivalente diretto
    return content


def needs_input_setup(content: str) -> bool:
    """Verifica se il file ha blocchi pyodide che usano input()."""
    # Cerca input( all'interno di blocchi pyodide
    in_pyodide = False
    for line in content.split("\n"):
        if re.match(r"```{pyodide-python}", line):
            in_pyodide = True
        elif line.startswith("```") and in_pyodide:
            in_pyodide = False
        elif in_pyodide and "input(" in line:
            return True
    return False


def add_input_setup(content: str) -> str:
    """Aggiunge blocco setup input() dopo il front matter."""
    # Trova la fine del front matter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            end = content.index("\n", end) + 1
            return content[:end] + "\n" + INPUT_SETUP_BLOCK + content[end:]
    # Se non c'è front matter, metti all'inizio
    return INPUT_SETUP_BLOCK + content


def convert_file(filepath: Path) -> Path:
    """Converte un singolo file .md in .qmd."""
    content = filepath.read_text(encoding="utf-8")

    # Applica conversioni in ordine
    content = convert_front_matter(content)
    content = convert_admonitions(content)
    content = convert_mermaid_fences(content)
    content = convert_pyodide_fences(content)
    content = convert_internal_links(content)
    content = convert_video_embeds(content)

    # Aggiungi setup input() se necessario (dopo conversione pyodide)
    if needs_input_setup(content):
        content = add_input_setup(content)

    # Scrivi file .qmd
    new_path = filepath.with_suffix(".qmd")
    new_path.write_text(content, encoding="utf-8")

    # Rimuovi vecchio .md
    if filepath != new_path and filepath.exists():
        filepath.unlink()

    return new_path


def main():
    """Converte tutti i file .md in docs/ in formato Quarto."""
    md_files = sorted(DOCS_DIR.rglob("*.md"))

    # Salta file che non devono essere convertiti
    skip = {"PDF_EXPORT_README.md"}
    md_files = [f for f in md_files if f.name not in skip]

    converted = 0
    for filepath in md_files:
        rel = filepath.relative_to(DOCS_DIR)
        new_path = convert_file(filepath)
        print(f"  {rel} → {new_path.relative_to(DOCS_DIR)}")
        converted += 1

    print(f"\nConvertiti {converted} file.")


if __name__ == "__main__":
    main()
