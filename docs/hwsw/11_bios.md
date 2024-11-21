# BIOS (Basic Input/Output System)

## Cos'è il BIOS?

Il **BIOS** (*Basic Input/Output System*) è un programma fondamentale del computer, memorizzato in una memoria speciale chiamata **ROM**. Si attiva automaticamente ogni volta che il computer viene acceso e gestisce le operazioni iniziali che permettono il corretto funzionamento dell'hardware.

## A cosa serve il BIOS?

Il BIOS ha il compito di:

1. **Avviare il sistema**: Controlla i componenti hardware (RAM, disco rigido, tastiera, ecc.) per assicurarsi che siano collegati e funzionino correttamente.
2. **Caricare il sistema operativo**: Dopo il controllo, il BIOS individua e carica il sistema operativo (come Windows o Linux) dal disco rigido o da un altro dispositivo di avvio.
3. **Gestire le impostazioni di sistema**: Consente di configurare alcuni parametri hardware importanti, come l’ordine di avvio, la frequenza della CPU, e la gestione di alcune periferiche.

## Come accedere al BIOS?

Per accedere al BIOS, è necessario premere un tasto specifico durante l’avvio del computer, prima che inizi a caricare il sistema operativo. Questo tasto può variare a seconda del produttore, ma i più comuni sono:

- **F2** o **F10**
- **DEL** (o **CANC**)
- **ESC**

> **Nota**: La schermata del BIOS può variare in base alla marca e al modello del computer. In genere, sulla prima schermata di avvio compare un messaggio con l’indicazione del tasto per entrare nel BIOS.

## Impostazioni principali modificabili nel BIOS

### 1. Sequenza di avvio (Boot Order)

La **sequenza di avvio** (o **boot order**) è un’impostazione del BIOS che permette di decidere l'ordine dei dispositivi da cui il computer prova ad avviarsi. 

Ecco i principali dettagli e utilizzi della sequenza di avvio:

- **Dispositivi comuni**: Includono disco rigido, unità USB, CD/DVD e, in alcuni casi, schede di rete.
  
- **Ordine di avvio**: Il BIOS verifica i dispositivi in base all'ordine specificato e tenta di avviare il sistema operativo dal primo dispositivo disponibile. L'ordine può essere modificato per dare la priorità a un particolare dispositivo.
  
- **Utilizzi principali**:
  - **Installazione del sistema operativo**: Se si vuole installare un sistema operativo da una chiavetta USB o un DVD, è necessario spostare quel dispositivo in cima all'ordine di avvio.
  - **Avvio da strumenti di riparazione**: In caso di problemi, è possibile avviare il computer da un disco o USB con programmi diagnostici.
  - **Sicurezza**: Si può limitare l’avvio ai soli dischi interni per evitare che il sistema venga avviato da dispositivi esterni non autorizzati.

> **Nota**: Modificare la sequenza di avvio è utile, ma richiede attenzione. Un ordine errato può impedire l'avvio corretto del sistema.

### 2. Data e ora

Permette di aggiornare la data e l'ora del sistema. Questo è importante, poiché alcuni processi di sistema, come l'accesso a file e la sincronizzazione di rete, dipendono dall’ora corretta.

### 3. Velocità della CPU e gestione energetica

Alcuni BIOS consentono di impostare la frequenza della CPU e le modalità di risparmio energetico. Queste impostazioni sono utili per ottimizzare le prestazioni del sistema o ridurre il consumo energetico, specialmente nei portatili.

### 4. Configurazione della memoria (RAM)

In alcuni BIOS avanzati è possibile impostare la velocità della RAM o attivare funzionalità speciali per migliorare le prestazioni del sistema.

### 5. Abilitazione/disabilitazione delle periferiche

Consente di abilitare o disabilitare alcune porte (come USB o audio) o componenti interni. Questa funzione è utile per disattivare temporaneamente periferiche non necessarie o risolvere problemi di compatibilità.

### 6. Gestione della sicurezza

Include opzioni per proteggere il BIOS con una password, limitando l’accesso a persone non autorizzate. Alcuni BIOS permettono anche di attivare la protezione contro l’avvio da dispositivi esterni.

## Informazioni Importanti sul BIOS

- **Modifica delle Impostazioni**: Le impostazioni del BIOS sono delicate. Apportare modifiche senza sapere esattamente cosa si sta facendo può causare problemi di avvio o di stabilità.
- **Aggiornamento del BIOS**: In alcuni casi, può essere necessario aggiornare il BIOS per migliorare la compatibilità con nuovi componenti hardware. Questo processo deve essere eseguito con attenzione.
- **Interfaccia UEFI**: Nei computer più recenti, il BIOS è stato in parte sostituito dall’**UEFI** (*Unified Extensible Firmware Interface*), che offre maggiori funzionalità e un’interfaccia grafica migliorata.

## Esempio di schermata del BIOS

Ecco un esempio di una tipica schermata del BIOS, che mostra alcune delle opzioni principali configurabili.

![Schermata BIOS](https://kmpic.asus.com/images/2022/07/21/e02270e4-b24f-4080-be10-674dde9db4f8.png)

> Divertiti con il [Simulatore di BIOS Lenovo](https://download.lenovo.com/bsco/index.html#/)

---

## Mappa Concettuale

```mermaid
graph LR
    A[BIOS Basic Input/Output System] --> B[Funzioni Principali]
    B --> C[Avvia il Sistema]
    B --> D[Controlla l'Hardware all'Avvio]
    B --> E[Carica il Sistema Operativo]
    B --> F[Gestisce le Impostazioni Hardware]

    A --> G[Accesso al BIOS]
    G --> H[Pulsanti di Accesso]
    H --> H1[F2]
    H --> H2[F10]
    H --> H3[DEL/CANC]
    H --> H4[ESC]

    A --> I[Impostazioni Principali]
    I --> J[Sequenza di Avvio]
    J --> J1[Dispositivi Comuni]
    J1 --> J1a[Disco Rigido]
    J1 --> J1b[USB]
    J1 --> J1c[CD/DVD]
    J1 --> J1d[Scheda di Rete]
    J --> J2[Ordine di Avvio]
    J --> J3[Utilizzi]
    J3 --> J3a[Installazione OS]
    J3 --> J3b[Strumenti di Riparazione]
    J3 --> J3c[Sicurezza]

    I --> K[Data e Ora]
    I --> L[Velocità della CPU]
    I --> M[Configurazione della Memoria]
    I --> N[Gestione delle Periferiche]
    I --> O[Sicurezza]

    A --> P[Informazioni Importanti]
    P --> Q[Modifica delle Impostazioni]
    P --> R[Aggiornamento del BIOS]
    P --> S[Interfaccia UEFI]
```
