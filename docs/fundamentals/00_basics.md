# Informatica – Concetti Generali

## Cos'è l'Informatica

La parola **«informatica»** è stata inventata nel **1957** da *Karl Steinbuch* e deriva da *informazione automatica*. Sì, nel 1957, quando i vostri nonni erano giovani e i computer occupavano intere stanze (e consumavano quanto un quartiere intero).

L'informatica è la **scienza che studia i metodi e le tecniche** per:

- **analizzare** i dati (tipo quando scrolli Instagram cercando quel meme che hai visto ieri),
- **rappresentarli** in modo comprensibile alle macchine (perché le macchine sono abbastanza tonterelle e capiscono solo 0 e 1),
- **elaborarli** (cioè farli "lavorare" da un computer),
- **organizzarli e trasmetterli** in modo efficiente.

> 💡 In sintesi, l'informatica serve per trasformare **informazioni** in **risultati utili**, in modo **automatico**. Tipo quando chiedi a ChatGPT di fare i compiti (ma non fatelo, eh).

---

## Come si rappresenta l’informazione

L’informazione, nel mondo digitale, si rappresenta con **numeri binari**, cioè formati solo da **0 e 1**.

### Il Bit

- Il termine **bit** viene da *binary digit* ("cifra binaria").
- È l'unità più piccola di informazione. Tipo l'atomo della materia, ma per i computer.
- Può assumere solo due valori: `0` oppure `1`.

> 💡 Il bit è come un interruttore: acceso (1) o spento (0). O come la vostra attenzione durante una lezione noiosa: c'è o non c'è, vie di mezzo non esistono.

### Combinazioni di più bit

Se usiamo più bit insieme possiamo rappresentare più informazioni.

| Numero di bit | Possibili combinazioni |
|----------------|------------------------|
| 1 bit | 2 (0, 1) |
| 2 bit | 4 (00, 01, 10, 11) |
| 3 bit | 8 |
| 8 bit (1 Byte) | 256 |

### Il Byte

- Un **byte (B)** è formato da **8 bit**.
- Serve per rappresentare un carattere (es. una lettera o un numero).

Esempio:

- La lettera **A** può essere rappresentata da una sequenza di 8 bit, ad esempio `01000001`.
- Praticamente il computer usa 8 interruttori per dire "A". Efficiente? Discutibile. Ma funziona!

---

## Che cos'è un Computer

Un **computer** è una **macchina elettronica** che elabora dati in modo **automatico e veloce**. Tipo un calcolatore super pompato che può anche guardare video di gattini.

### Fasi di funzionamento

1. **Input** → immissione dei dati (es. tastiera, mouse, microfono). Tu fai qualcosa.
2. **Elaborazione** → esecuzione del programma (da parte della CPU). Il computer pensa intensamente.
3. **Output** → restituzione del risultato (es. monitor, stampante). Il computer ti risponde (speriamo bene).

> 🧠 Il computer non ha intelligenza propria: segue solo le **istruzioni** che gli diamo noi! Se fa cose strane, probabilmente è colpa di chi l'ha programmato. Quindi non prendetevela col PC quando si pianta!

---

## Le Due Parti Fondamentali di un Computer

### Hardware

È la **parte fisica** del computer, cioè tutto ciò che si può toccare (ma non rompete, please).
Esempi:

- CPU (processore) - il cervello del computer
- Memoria RAM - la memoria a breve termine (tipo quando studiate la sera prima dell'interrogazione)
- Hard disk o SSD - la memoria a lungo termine (dove conservate le foto imbarazzanti)
- Tastiera, mouse, monitor, stampante

### Software

È la **parte logica**, cioè l'insieme dei programmi e delle istruzioni che permettono di usare l'hardware.
Esempi:

- Sistema operativo (Windows, Linux, macOS) - il "direttore d'orchestra" del computer
- Applicazioni (Word, Browser, TikTok... ops, quello forse non lo diciamo al prof)

> 💡 Hardware e software **dipendono l'uno dall'altro**: senza hardware il software non funziona, e viceversa! È come il corpo e la mente: servono entrambi per funzionare.

---

## Tipologie di Computer

Oggi esistono molte forme di computer, ma il loro funzionamento è simile. Sono tutti computer travestiti!

- **PC (Desktop o Tower)** → il classicone, usato a casa o a scuola. Quello grosso sotto la scrivania che fa da poggiapiedi.
- **Laptop o Notebook** → portatile, perfetto per fingersi produttivi al bar mentre si guarda Netflix.
- **Tablet** → schermo touch, senza tastiera fisica. Ottimo per disegnare o per far vedere le foto ai nonni.
- **Smartphone** → il computer che sta in tasca e che controllate ogni 30 secondi (be honest).
- **Server** → computer che fornisce dati o servizi ad altri, spesso chiuso in stanze piene di ventole rumorose. Sono i veri eroi che fanno funzionare Internet mentre voi guardate meme.

---

## Le Memorie del Computer

Le **memorie** servono a **conservare i dati** (in modo temporaneo o permanente). Tipo i cassetti della vostra scrivania, ma digitali.

| Tipo di memoria | Significato | Caratteristiche |
|------------------|-------------|------------------|
| **ROM** | Read Only Memory | Solo lettura, contiene istruzioni permanenti (tipo le regole della scuola: ci sono e basta) |
| **RAM** | Random Access Memory | Veloce ma smemorata: si svuota quando si spegne il PC. Come voi dopo una festa. |
| **HDD/SSD** | Disco fisso o unità a stato solido | Memoria permanente, conserva dati e programmi (anche dopo lo spegnimento, wow!) |

> 📦 Più memoria = più dati immagazzinabili = più foto, musica, giochi, video...
> ⚡ Più velocità = elaborazioni più rapide = meno tempo ad aspettare che si carichi tutto!

---

## Linguaggio Macchina

Il **linguaggio macchina** è l'unico linguaggio che la **CPU** capisce direttamente.
È scritto in **codice binario** (0 e 1). Praticamente il computer parla solo in "sì" e "no".

Esempio: `10110000 01100001`

Ogni sequenza rappresenta un'**istruzione** per il processore. Tipo: "prendi questo numero, sommalo a quest'altro, mettilo qui". Ma in binario.

> 👨‍💻 I linguaggi di programmazione "umani" (Python, C, ecc.) vengono tradotti in linguaggio macchina dal compilatore o interprete. È tipo avere un traduttore simultaneo tra voi e il computer. Comodo, no?

---

## Multipli delle Unità Informatiche

In informatica si usano multipli del byte basati su potenze di 2. Perché gli informatici amano complicarsi la vita.

| Unità | Simbolo | Valore esatto | Valore approssimato |
|--------|----------|---------------|----------------------|
| **Kilobyte** | KB | 2¹⁰ B = 1.024 B | ≈ 1.000 B (un file di testo corto) |
| **Megabyte** | MB | 2²⁰ B = 1.048.576 B | ≈ 1.000.000 B (una foto decente) |
| **Gigabyte** | GB | 2³⁰ B = 1.073.741.824 B | ≈ 1.000.000.000 B (un film, tipo) |

> ⚠️ In realtà i nomi corretti sarebbero **kibibyte (KiB)**, **mebibyte (MiB)** e **gibibyte (GiB)**, ma comunemente si usano KB, MB e GB. Perché "mebibyte" suona ridicolo e nessuno lo usa tranne i puristi dell'informatica.

---

## Riepilogo Finale

| Concetto | Significato |
|-----------|-------------|
| **Informatica** | Scienza dell’elaborazione automatica delle informazioni |
| **Bit** | Unità minima di informazione (0 o 1) |
| **Byte** | Gruppo di 8 bit |
| **Computer** | Macchina elettronica per elaborare dati |
| **Hardware** | Parte fisica del computer |
| **Software** | Parte logica: programmi e istruzioni |
| **CPU** | Unità centrale di elaborazione |
| **Memoria** | Dispositivi per immagazzinare dati |
| **Linguaggio macchina** | Codice binario compreso dalla CPU |

---

> ✨ **Obiettivo dell'informatica:** usare le macchine per gestire e trasformare informazioni in modo automatico, veloce e preciso. Praticamente far fare alle macchine il lavoro noioso al posto nostro. Il sogno!
