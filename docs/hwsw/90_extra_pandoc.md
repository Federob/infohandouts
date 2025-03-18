
# Dispensa: Guida a Pandoc e Markdown per Relazioni Scientifiche

## Introduzione

Pandoc è uno strumento open source che consente di trasformare file Markdown in diversi formati, tra cui PDF. È particolarmente utile per scrivere e formattare relazioni scientifiche in modo chiaro ed efficace.

## Installazione di Pandoc

- Scarica Pandoc dal sito ufficiale: [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
- Installa anche LaTeX:
  - Windows: [MiKTeX](https://miktex.org/download)
  - macOS: [MacTeX](https://www.tug.org/mactex/)

Verifica l'installazione digitando nel terminale:
```
pandoc --version
```

## Struttura base di una relazione scientifica in Markdown

### Esempio:

# Titolo della relazione

## Autore
Nome Cognome, Classe, Data

## Abstract
Riassunto sintetico dell'intera relazione.

## Introduzione
Introduzione all'argomento trattato.

## Materiali e Metodi
Descrizione dei materiali e metodi utilizzati.

## Risultati
Esposizione chiara e oggettiva dei risultati ottenuti.

## Discussione
Analisi critica e interpretazione dei risultati.

## Conclusioni
Riassunto conclusivo degli obiettivi raggiunti.

## Bibliografia
- [1] Autore, Titolo, Rivista, Anno.

## Conversione del documento Markdown in PDF

Per convertire il tuo documento in PDF, apri il terminale e digita:

```
pandoc relazione.md -o relazione.pdf
```

## Formattazioni avanzate per relazioni scientifiche

- **Indice automatico:**
```
pandoc relazione.md --toc -o relazione.pdf
```

- **Margini personalizzati:**
```
pandoc relazione.md -V geometry:"margin=2cm" -o relazione.pdf
```

- **Numeri di pagina automatici:**
```
pandoc relazione.md -V pagestyle=plain -o relazione.pdf
```

- **Utilizzo di formule matematiche:**
Puoi usare LaTeX all'interno del markdown:
```
La formula di Einstein è $E=mc^2$
```

## Template avanzato con Pandoc

Per layout scientifici complessi puoi usare un template LaTeX:

```
pandoc relazione.md --template=scientific-template.tex -o relazione.pdf
```

Scarica o crea il tuo template LaTeX e salvalo nella stessa cartella del file markdown.

## Consigli utili:

- Usa un editor markdown come [Typora](https://typora.io/) o [Visual Studio Code](https://code.visualstudio.com/).
- Controlla sempre la corretta visualizzazione del PDF finale.

---

Ora sei pronto per scrivere e convertire le tue relazioni scientifiche usando Markdown e Pandoc!

Buon lavoro!
