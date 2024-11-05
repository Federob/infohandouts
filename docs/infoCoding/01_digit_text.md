# La Codifica del Testo: ASCII e Unicode

La **codifica del testo** è un sistema che associa un insieme di simboli a dei valori numerici, permettendo ai computer di memorizzare e interpretare il testo. Senza un sistema di codifica, un computer non sarebbe in grado di capire se una sequenza di bit rappresenta una lettera, un numero o un simbolo speciale.

## 1. ASCII: American Standard Code for Information Interchange

**ASCII** è uno dei primi standard di codifica del testo, sviluppato negli anni '60. Utilizza 7 bit per rappresentare 128 simboli unici, che includono:
- Lettere maiuscole e minuscole (A-Z, a-z)
- Numeri (0-9)
- Simboli speciali (come `!`, `@`, `#`, ecc.)
- Caratteri di controllo, come `Enter` (codice 13) o `Tab` (codice 9)

### Tabella dei Caratteri ASCII

| Simbolo | Codice Decimale | Codice Binario |
|---------|------------------|----------------|
| A       | 65               | 01000001       |
| B       | 66               | 01000010       |
| a       | 97               | 01100001       |
| b       | 98               | 01100010       |
| 0       | 48               | 00110000       |
| 1       | 49               | 00110001       |
| @       | 64               | 01000000       |
| !       | 33               | 00100001       |


![ASCII](https://upload.wikimedia.org/wikipedia/commons/d/dd/ASCII-Table.svg)

### Limiti di ASCII

ASCII funziona bene per l'inglese e alcune lingue europee, ma non è adatto per rappresentare simboli di altre lingue, come le lettere accentate francesi o i caratteri cinesi. Per questo, si è sviluppata una codifica più estesa, chiamata **Unicode**.

## 2. Unicode: Un Codice Universale

**Unicode** è uno standard di codifica che include simboli da quasi tutte le lingue del mondo. Unicode assegna un numero univoco a ogni simbolo, chiamato **punto di codice**. Ad esempio:
- Il carattere `A` ha il punto di codice U+0041.
- Il simbolo `Ω` (Omega) ha il punto di codice U+03A9.

Unicode supporta oltre un milione di simboli, coprendo lingue antiche e moderne, emoji, simboli matematici e molto altro.

### UTF-8: Una Codifica di Unicode

Uno dei formati più usati per rappresentare Unicode è **UTF-8**:
- **UTF-8** è una codifica variabile, che utilizza da 1 a 4 byte per ogni simbolo.
- È compatibile con ASCII: tutti i simboli ASCII occupano 1 byte in UTF-8 e hanno lo stesso valore numerico.

Questa caratteristica rende UTF-8 ideale per documenti e pagine web, permettendo di rappresentare testo in diverse lingue mantenendo la compatibilità con il testo ASCII.

## 3. Differenze tra ASCII e Unicode

| Caratteristica        | ASCII                                | Unicode                         |
|-----------------------|--------------------------------------|---------------------------------|
| Bit utilizzati        | 7 bit (128 simboli)                 | Variabile (UTF-8, UTF-16, ecc.) |
| Supporto per lingue   | Solo inglese e simboli base         | Tutte le lingue e simboli       |
| Compatibilità UTF-8   | Compatibile                         | UTF-8 è una codifica di Unicode |
| Utilizzo principale   | Vecchi sistemi e dati semplici      | Pagine web, applicazioni moderne|

## Esempio di Codifica

Immaginiamo di voler rappresentare la parola "Ciao" in UTF-8. Le lettere hanno i seguenti punti di codice in Unicode:
- `C` → U+0043
- `i` → U+0069
- `a` → U+0061
- `o` → U+006F

UTF-8 rappresenterà ciascuno di questi caratteri in modo efficiente, con un solo byte per carattere, poiché rientrano nei valori ASCII.

## Perché è Importante la Codifica del Testo?

La codifica del testo è fondamentale per la comunicazione globale e per il corretto funzionamento di applicazioni software e pagine web. Con Unicode e UTF-8, possiamo rappresentare testi in qualsiasi lingua e utilizzare simboli e emoji, mantenendo la compatibilità con ASCII.

### Esercizi

1. Scrivi il codice binario per i caratteri `C` e `i` utilizzando la codifica ASCII.
2. Qual è il punto di codice Unicode per la lettera `ñ`? (Suggerimento: cerca nella tabella Unicode)
3. Converti la frase "Hello!" in binario usando la codifica ASCII.

