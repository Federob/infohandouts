#!/bin/bash
# ============================================================
# Setup per il progetto Quarto - Corso di Informatica
# ============================================================
#
# Prerequisiti:
#   1. Quarto installato: https://quarto.org/docs/get-started/
#      Verifica con: quarto --version
#
# Uso:
#   chmod +x setup_quarto.sh
#   ./setup_quarto.sh
#
# ============================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}=== Setup progetto Quarto ===${NC}"
echo ""

# Verifica che Quarto sia installato
if ! command -v quarto &> /dev/null; then
    echo -e "${RED}ERRORE: Quarto non trovato!${NC}"
    echo "Installa Quarto da: https://quarto.org/docs/get-started/"
    exit 1
fi

QUARTO_VER=$(quarto --version)
echo -e "Quarto versione: ${GREEN}${QUARTO_VER}${NC}"
echo ""

# Vai nella directory docs/ (root del progetto Quarto)
cd "$(dirname "$0")/docs"
echo "Directory progetto: $(pwd)"
echo ""

# Installa estensione quarto-pyodide per Python interattivo
echo -e "${YELLOW}Installando estensione quarto-pyodide...${NC}"
if [ -d "_extensions/coatless/pyodide" ]; then
    echo "  Già installata, aggiornamento..."
    quarto add coatless/quarto-pyodide --no-prompt || true
else
    quarto add coatless/quarto-pyodide --no-prompt
fi
echo -e "${GREEN}  OK${NC}"
echo ""

# Preview del sito
echo -e "${GREEN}=== Setup completato! ===${NC}"
echo ""
echo "Comandi utili:"
echo "  cd docs"
echo "  quarto preview              # Avvia preview locale"
echo "  quarto render               # Build del sito"
echo "  quarto publish gh-pages     # Deploy su GitHub Pages"
echo ""
echo -e "${YELLOW}NOTA:${NC} L'estensione pyodide richiede connessione internet"
echo "      al primo caricamento (scarica Pyodide ~20MB)."
