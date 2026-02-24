#!/bin/bash
#
# Script di deploy locale per infohandouts
# Sostituisce la GitHub Action (ci.yml)
#
# Uso: ./deploy.sh [messaggio commit] [--force-pdf]
# Esempio: ./deploy.sh "aggiunta sezione IA"
# Esempio: ./deploy.sh "rebuild" --force-pdf    (rigenera tutti i PDF)
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

# Salva il branch corrente per verificare alla fine
ORIGINAL_BRANCH=$(git branch --show-current)

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Deploy infohandouts${NC}"
echo -e "${BLUE}  Branch: ${ORIGINAL_BRANCH}${NC}"
echo -e "${BLUE}========================================${NC}"

# Funzione di cleanup in caso di errore
cleanup() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo -e "\n${RED}  ✗ Errore durante il deploy (exit code: $exit_code)${NC}"
        # Assicurati di essere sul branch originale
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
echo -e "\n${YELLOW}[1/7] Verifica prerequisiti...${NC}"

if [ ! -d "infoenv" ]; then
    echo -e "${RED}  ✗ infoenv/ non trovato! Crea il venv con: python3 -m venv infoenv${NC}"
    exit 1
fi

source infoenv/bin/activate
echo -e "${GREEN}  ✓ venv attivato ($(python --version))${NC}"

# Verifica che le dipendenze siano installate
python -c "import mkdocs; import material; import markdown_exec" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}  ✗ Dipendenze mancanti! Installa con:${NC}"
    echo -e "${RED}    pip install mkdocs-material mkdocs-mermaid2-plugin mkdocs-video 'markdown-exec[ansi]' requests${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ dipendenze OK${NC}"

# Verifica che non ci siano modifiche non committate nei file critici
if ! git diff --quiet mkdocs.yml 2>/dev/null; then
    echo -e "${YELLOW}  ⚠ mkdocs.yml ha modifiche non staged (verranno incluse nel commit)${NC}"
fi

# -------------------------------------------
# 2. Genera il file Google IP ranges
# -------------------------------------------
echo -e "\n${YELLOW}[2/7] Generazione Google IP ranges...${NC}"
python code/googleiprangeparser.py --output docs/extra/googleipranges.txt
echo -e "${GREEN}  ✓ googleipranges.txt generato${NC}"

# -------------------------------------------
# 3. Genera i PDF
# -------------------------------------------
echo -e "\n${YELLOW}[3/7] Generazione PDF (incrementale)...${NC}"
python code/generate_pdfs.py $FORCE_PDF
echo -e "${GREEN}  ✓ PDF aggiornati${NC}"

# -------------------------------------------
# 4. Build del sito
# -------------------------------------------
echo -e "\n${YELLOW}[4/7] Build del sito MkDocs...${NC}"
mkdocs build
echo -e "${GREEN}  ✓ Build completato${NC}"

# -------------------------------------------
# 5. Commit su main (se ci sono modifiche)
# -------------------------------------------
echo -e "\n${YELLOW}[5/7] Commit delle modifiche su ${ORIGINAL_BRANCH}...${NC}"

# Parsing argomenti
COMMIT_MSG="deploy"
FORCE_PDF=""
for arg in "$@"; do
    if [ "$arg" = "--force-pdf" ]; then
        FORCE_PDF="--force"
    else
        COMMIT_MSG="$arg"
    fi
done

git add -A

if git diff --cached --quiet; then
    echo -e "${YELLOW}  ⚠ Nessuna modifica da committare${NC}"
else
    git commit -m "$COMMIT_MSG"
    echo -e "${GREEN}  ✓ Commit creato: $COMMIT_MSG${NC}"
fi

# -------------------------------------------
# 6. Push su main
# -------------------------------------------
echo -e "\n${YELLOW}[6/7] Push su ${ORIGINAL_BRANCH}...${NC}"
git push origin "$ORIGINAL_BRANCH"
echo -e "${GREEN}  ✓ Push su ${ORIGINAL_BRANCH} completato${NC}"

# -------------------------------------------
# 7. Deploy su GitHub Pages (branch gh-pages)
# -------------------------------------------
echo -e "\n${YELLOW}[7/7] Deploy su GitHub Pages (gh-pages)...${NC}"
mkdocs gh-deploy --force
echo -e "${GREEN}  ✓ Deploy su gh-pages completato${NC}"

# -------------------------------------------
# Verifica finale: siamo ancora sul branch giusto?
# -------------------------------------------
FINAL_BRANCH=$(git branch --show-current)
if [ "$FINAL_BRANCH" != "$ORIGINAL_BRANCH" ]; then
    echo -e "${YELLOW}  ⚠ Branch cambiato! Ripristino ${ORIGINAL_BRANCH}...${NC}"
    git checkout "$ORIGINAL_BRANCH"
fi

echo -e "\n${BLUE}========================================${NC}"
echo -e "${GREEN}  Deploy terminato con successo!${NC}"
echo -e "${GREEN}  Branch corrente: $(git branch --show-current)${NC}"
echo -e "${BLUE}========================================${NC}"
