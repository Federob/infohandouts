# I File: cosa sono e a cosa servono

Un **file** è una raccolta di dati memorizzata in un dispositivo di archiviazione, come un computer o una chiavetta USB. I file consentono di organizzare le informazioni in modo strutturato e accessibile per permettere ai programmi di leggerle, modificarle o condividerle con altri dispositivi e utenti.

## A cosa servono i File

I file sono fondamentali per:

- **Memorizzare Dati**: come documenti di testo, immagini, audio e video.
- **Scambio di Informazioni**: consentono di trasferire dati tra diversi computer e applicazioni.
- **Organizzazione**: mantengono i dati separati e strutturati in modo che possano essere facilmente trovati e gestiti.

## Tipi di File e le Estensioni Principali

Ogni file ha un'**estensione** alla fine del nome (ad esempio, `.txt` o `.jpg`), che indica il formato e permette ai programmi di riconoscere come aprirlo.

### File di Testo

I file di testo contengono solo caratteri leggibili, come lettere e numeri. Alcune delle estensioni principali includono:

- **.txt** – Testo semplice, senza formattazione.
- **.docx** – Documento di Microsoft Word.
- **.pdf** – Formato di documento portatile, utilizzato per documenti finalizzati alla condivisione.
- **.csv** – File di valori separati da virgola, usato per dati strutturati (spesso importati in fogli di calcolo).

### File Immagine

I file di immagine memorizzano dati visivi in vari formati. Alcune delle estensioni principali includono:

- **.jpg** o **.jpeg** – Formato compresso, molto usato per le foto.
- **.png** – Formato senza perdita di qualità, con supporto per trasparenza.
- **.gif** – Formato per immagini animate, con colori limitati.
- **.bmp** – Bitmap, un formato non compresso usato per immagini di alta qualità.

### File Audio

I file audio memorizzano suoni come voce, musica o altri effetti sonori. Alcune delle estensioni principali includono:

- **.mp3** – Formato compresso, usato per la musica digitale.
- **.wav** – Formato non compresso, usato per audio di alta qualità.
- **.aac** – Formato audio avanzato, usato per file compressi.

### File Video

I file video memorizzano immagini in movimento, spesso accompagnate da suoni. Alcune delle estensioni principali includono:

- **.mp4** – Formato di compressione video popolare, compatibile con molti dispositivi
- **.avi** – Formato video standard, con qualità alta ma file di grandi dimensioni
- **.mov** – Formato usato per i video Apple, compatibile con i sistemi macOS

[Scopri com'è fatto un file all'interno!!](https://hexed.it/)

## Bitrate

Il **bitrate** indica quanti bit vengono trasmessi ogni secondo nei file video o nei file audio. Si misura in **kbps** (kilobit al secondo) o **Mbps** (megabit al secondo). Un bitrate più alto generalmente indica una qualità audio/video migliore, ma anche file più grandi.

Il **bitrate  di un video** è dato dalla formula (teorica) : **risoluzione (formato) * profondità di colore * fps (numero di frame ogni secondo)**

Il **bitrate di un file audio** è dato dalla formula (teorica) : **risoluzione (numero di bit per ogni campione) * frequenza di campionamento**

L' **occupazione di memoria** dei file audio e video è data dalla formula (teorica) : **bitrate * durata (in secondi)** , mentre quella delle immagini è data dalla formula : **risoluzione * profondità di colore**


> N.B. : Le formule sono teoriche perché non vengono considerate le compressioni, che ottengono sempre come risultato la diminuzione dell'occupazione di memoria teorica stimata

### Esempi

- Un video 1080p con un bitrate di 4 Mbps sarà più nitido rispetto allo stesso video con un bitrate di 2 Mbps (dovuto magari ad un numero di fps più elevato)
- Un video 4K richiede solitamente un bitrate più alto rispetto a un video HD per mantenere la stessa qualità.
- Il bitrate teorico di un file audio campionato a 44.1 kHz e risoluzione 16 bit è di 705.6 kbps

## Compressione dei file multimediali (Immagini, Audio, Video)

La **compressione** riduce la dimensione del file eliminando informazioni ridondanti. Ci sono due principali tipi di compressione:

- **Compressione senza perdita di dati (lossless)**: riduce la dimensione del file senza perdere qualità. Ad esempio *elimina i dati ridondanti*, ma non è molto efficiente per i video.
- **Compressione con perdita di dati (lossy)**: elimina parte delle informazioni per ridurre la dimensione del file. E' la più comune per i video e gli audio.

## Mappa Concettuale

```mermaid
graph LR
    A[File] --> B[Testo]
    A --> C[Immagine]
    A --> D[Audio]
    A --> E[Video]

    B --> B1[.txt]
    B --> B2[.docx]
    B --> B3[.pdf]
    B --> B4[.csv]

    C --> C1[.jpg/.jpeg]
    C --> C2[.png]
    C --> C3[.gif]
    C --> C4[.bmp]

    D --> D1[.mp3]
    D --> D2[.wav]
    D --> D3[.aac]
    D --> BTA[Bitrate bps]
    BTA --> BTA1[Risoluzione]
    BTA --> BTA2[Frequenza di campionamento]

    E --> E1[.mp4]
    E --> E2[.avi]
    E --> E3[.mov]
    D --> BTV[Bitrate bps]
    BTV --> BTV1[Risoluzione/Formato]
    BTV --> BTV2[Fps]
    BTV --> BTV3[Profondità di colore]

    A --> I[Compressione Immagini, Audio, Video]
    I --> J[Compressione Lossless]
    I --> K[Compressione Lossy]
```
