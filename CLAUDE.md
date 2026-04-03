# CLAUDE.md - Progetto infohandouts

## Panoramica

Sito didattico **"Corso di Informatica"** del Prof. Federico Robuffo, pubblicato su GitHub Pages.
Contiene dispense per studenti su: fondamenti informatici, hardware/software, codifica delle informazioni, algoritmi, Python, intelligenza artificiale.

- **URL**: https://federob.github.io/infohandouts/
- **Framework**: [Quarto](https://quarto.org/) (website project)
- **Lingua dei contenuti**: italiano

## Struttura del progetto

```
docs/                    # Root del progetto Quarto
  _quarto.yml            # Configurazione Quarto (sidebar, navbar, formato)
  index.qmd              # Landing page
  fundamentals/          # Concetti base e mappe concettuali
  hwsw/                  # Hardware, software, OS, CLI
  infoCoding/            # Codifica: testo, immagini, audio, video, file
  algocoding/            # Algoritmi, Flowgorithm, cheatsheet Python
  pycoding/              # Corso Python (variabili -> oggetti -> networking)
  ai/                    # Corso IA/ML (intro -> reti neurali -> etica)
  dictionary/            # Glossario e mappa dei termini
  extra/                 # Attivita extra (giochi, curiosita)
  _extensions/           # Estensioni Quarto (pyodide per Python interattivo)
  _filters/              # Filtri Lua custom (mermaid-config)
  _site/                 # Output generato (non editare)
  stylesheets/           # CSS custom (mermaid dark, Monaco editor)
  custom.scss            # Override tema
code/                    # Script Python di supporto
deploy.sh                # Script di deploy: commit + push + quarto publish gh-pages
setup_quarto.sh          # Setup iniziale (installa estensione pyodide)
```

## Comandi principali

```bash
# Preview locale
cd docs && quarto preview

# Build sito
cd docs && quarto render

# Deploy completo (commit + push main + publish gh-pages)
./deploy.sh "messaggio commit"

# Setup iniziale (installa estensioni)
./setup_quarto.sh
```

## Convenzioni contenuti

- I file `.qmd` sono Quarto Markdown (YAML frontmatter + Markdown + code blocks)
- Naming: `NN_nome.qmd` dove NN e un numero a due cifre per l'ordinamento
- La struttura delle sidebar e definita in `docs/_quarto.yml`
- I diagrammi usano Mermaid (con filtro Lua per configurazione dark mode)
- Il codice Python interattivo nel browser usa l'estensione `quarto-pyodide`
- Il tema HTML supporta light (cosmo) e dark (darkly), entrambi con `custom.scss`
- Il deploy avviene sul branch `gh-pages` tramite `quarto publish`

## Linee guida per le modifiche

- **Nuove pagine**: creare il `.qmd` nella cartella tematica e aggiungere il riferimento in `_quarto.yml` nella sidebar appropriata
- **Immagini**: posizionare nella stessa cartella del `.qmd` che le referenzia
- **Tono**: informale e accessibile, adatto a studenti. Il sito usa un tono leggero e a tratti ironico
- **Lingua**: tutto in italiano, inclusi commenti nel codice d'esempio
- **Formato date**: DD/MM/YYYY (configurato in `_quarto.yml`)
- **Footer**: aggiornare l'anno nel copyright in `_quarto.yml` se necessario
