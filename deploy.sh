#!/bin/bash
#
# Script di deploy per infohandouts (Quarto)
#
# Uso: ./deploy.sh [messaggio commit]
# Esempio: ./deploy.sh "aggiunta sezione IA"
#

# Colori
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Directory del progetto
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

ORIGINAL_BRANCH=$(git branch --show-current)

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Deploy infohandouts (Quarto)${NC}"
echo -e "${BLUE}  Branch: ${ORIGINAL_BRANCH}${NC}"
echo -e "${BLUE}========================================${NC}"

cleanup() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo -e "\n${RED}  ✗ Errore durante il deploy (exit code: $exit_code)${NC}"
        CURRENT=$(git branch --show-current)
        if [ "$CURRENT" != "$ORIGINAL_BRANCH" ]; then
            echo -e "${YELLOW}  Ripristino branch ${ORIGINAL_BRANCH}...${NC}"
            git checkout "$ORIGINAL_BRANCH"
        fi
    fi
}
trap cleanup EXIT

set -e

# -------------------------------------------
# 1. Verifica prerequisiti
# -------------------------------------------
echo -e "\n${YELLOW}[1/3] Verifica prerequisiti...${NC}"

if ! command -v quarto &> /dev/null; then
    echo -e "${RED}  ✗ Quarto non trovato! Installa da: https://quarto.org/docs/get-started/${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ Quarto $(quarto --version)${NC}"

# -------------------------------------------
# 2. Commit e push su main
# -------------------------------------------
echo -e "\n${YELLOW}[2/3] Commit e push su ${ORIGINAL_BRANCH}...${NC}"

COMMIT_MSG="${1:-deploy}"

git add -A

if git diff --cached --quiet; then
    echo -e "${YELLOW}  ⚠ Nessuna modifica da committare${NC}"
else
    git commit -m "$COMMIT_MSG"
    echo -e "${GREEN}  ✓ Commit creato: $COMMIT_MSG${NC}"
fi

git push origin "$ORIGINAL_BRANCH"
echo -e "${GREEN}  ✓ Push su ${ORIGINAL_BRANCH} completato${NC}"

# -------------------------------------------
# 3. Deploy su GitHub Pages (render + publish)
# -------------------------------------------
echo -e "\n${YELLOW}[3/3] Build e deploy su GitHub Pages (gh-pages)...${NC}"
cd docs
quarto publish gh-pages --no-browser --no-prompt
cd "$SCRIPT_DIR"
echo -e "${GREEN}  ✓ Deploy su gh-pages completato${NC}"

# Verifica branch finale
FINAL_BRANCH=$(git branch --show-current)
if [ "$FINAL_BRANCH" != "$ORIGINAL_BRANCH" ]; then
    echo -e "${YELLOW}  ⚠ Ripristino ${ORIGINAL_BRANCH}...${NC}"
    git checkout "$ORIGINAL_BRANCH"
fi

echo -e "\n${BLUE}========================================${NC}"
echo -e "${GREEN}  Deploy terminato con successo!${NC}"
echo -e "${GREEN}  Branch corrente: $(git branch --show-current)${NC}"
echo -e "${BLUE}========================================${NC}"
