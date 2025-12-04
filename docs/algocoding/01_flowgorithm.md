# Codificare un algoritmo con Flowgorithm

## 1. Introduzione a Flowgorithm

**Flowgorithm** è un ambiente visuale che permette di creare algoritmi con **diagrammi di flusso** (tipo flowchart).

È perfetto per capire la logica della programmazione SENZA dover scrivere codice vero. È tipo disegnare invece di scrivere: più intuitivo e meno frustrante per chi inizia!

Praticamente è la modalità "easy" della programmazione. Una volta capito il concetto, passare a linguaggi veri (Python, Java, C++) sarà molto più semplice.

---

## 2. Download e installazione

### Versione "Executable Only" (consigliata)

La versione più comoda: **non richiede installazione**! Basta scaricare lo ZIP, estrarlo e avviare l'eseguibile. Zero sbattimenti.

📥 **Download**: [Clicca qui per scaricare Flowgorithm](https://flowgorithm.org/download/index.html)

Dopo aver estratto, eseguite:

```bash
Flowgorithm.exe
```

E siete pronti a programmare!

---

## 3. Blocchi principali di Flowgorithm

I diagrammi di flusso sono fatti di **blocchi** (forme geometriche) collegati tra loro. Ogni blocco ha un ruolo preciso.

---

### 3.1 **Declare – Dichiarazione variabili**

Serve a **creare variabili** e specificare il tipo di dato (numero intero, decimale, testo, vero/falso).

```mermaid
flowchart LR
    A["Blocco DECLARE:<br/>crea variabili e specifica il tipo (Integer, Real, String, Boolean)"]
```

---

### 3.2 **Input – Acquisizione dati**

Chiede all'utente di inserire un valore (tipo "Inserisci la tua età").

**Pro tip**: prima dell'Input mettete sempre un blocco Output che spiega COSA deve inserire l'utente. Altrimenti l'utente si ritrova una finestra vuota e pensa "Cosa devo scrivere???"

```mermaid
flowchart LR
    A["Output: istruzione per l'utente"] --> B[/"Input: legge il valore inserito"/]
```

---

### 3.3 **Assign – Assegnazione**

Fa **calcoli** e assegna il risultato a una variabile. Tipo: `area = base * altezza`. Questo è il blocco dove avviene la "magia matematica".

```mermaid
flowchart LR
    A["Valori disponibili"] --> B["Blocco ASSIGN:<br/>esegue calcoli o aggiorna variabili"]
```

---

### 3.4 **Output – Stampa risultati**

Mostra un testo o un valore a schermo.

```mermaid
flowchart LR
    A["Valore o messaggio"] --> B[/"Blocco OUTPUT:<br/>visualizza il contenuto"/]
```

---

### 3.5 **If – Struttura condizionale**

Permette di scegliere diversi percorsi in base a una condizione.

```mermaid
flowchart TD
    B{"Verifica della condizione"} -->|Sì| C["Ramo VERO"]
    B -->|No| D["Ramo FALSO"]
```

---

## 4. Analisi del problema

### Problema

Calcolare:

- l’area di un trapezio (base maggiore, base minore, altezza)  
- l’area di un cerchio (raggio)  

e confrontarle per stabilire quale sia maggiore.

---

## 4.1 Come si individuano input, elaborazioni, output e condizioni

### **1) Individuazione degli INPUT**

Gli input sono dati **necessari** per partire e non ottenibili tramite calcoli.

Dal testo otteniamo:

- baseMaggiore  
- baseMinore  
- altezza  
- raggio  

### **2) Individuazione delle ELABORAZIONI**

Ogni formula richiede una variabile dedicata:

- `area_trapezio = (baseMaggiore + baseMinore) / 2 * altezza`  
- `area_cerchio = 3.14 * raggio * raggio`

Variabili generate:

- area_trapezio  
- area_cerchio  

### **3) Individuazione degli OUTPUT**

Il programma deve comunicare:

- area del trapezio  
- area del cerchio  
- quale area è maggiore

### **4) Individuazione delle CONDIZIONI**

Confronto:

```
area_trapezio > area_cerchio
```

Questa condizione non crea nuove variabili: usa quelle già esistenti.

---

## 4.2 Diagramma degli stati

```mermaid
stateDiagram-v2
    [*] --> Titolo
    Titolo --> IstruzioniInput
    IstruzioniInput --> LetturaBmag
    LetturaBmag --> LetturaBmin
    LetturaBmin --> LetturaH
    LetturaH --> LetturaR
    LetturaR --> CalcoloAreaTrapezio
    CalcoloAreaTrapezio --> CalcoloAreaCerchio
    CalcoloAreaCerchio --> VerificaUguaglianza

    VerificaUguaglianza --> AreeUguali: area trapezio = area cerchio
    VerificaUguaglianza --> VerificaMaggiore: area trapezio <> area cerchio

    VerificaMaggiore --> TrapezioMaggiore: area trapezio > area cerchio
    VerificaMaggiore --> CerchioMaggiore: area cerchio > area trapezio

    AreeUguali --> OutputRisultato
    TrapezioMaggiore --> OutputRisultato
    CerchioMaggiore --> OutputRisultato

    OutputRisultato --> [*]
```

---

## 4.3 Flowchart dettagliato

```mermaid
flowchart TD

    classDef startend fill:#F2F2F2,stroke:#4A4A4A,stroke-width:1,color:#000
    classDef input fill:#F2F2F2,stroke:#4A4A4A,stroke-width:1,color:#000
    classDef output fill:#F2F2F2,stroke:#4A4A4A,stroke-width:1,color:#000
    classDef assign fill:#F2F2F2,stroke:#4A4A4A,stroke-width:1,color:#000
    classDef decision fill:#F2F2F2,stroke:#4A4A4A,stroke-width:1,color:#000

    A[\"Output: Questo programma calcola e confronta le aree di un trapezio e un cerchio"\]:::output --> 
    B[\"Output: Inserisci la base maggiore del trapezio"\]:::output --> C[/Input base maggiore/]:::input

    C --> D[\"Output: Inserisci la base minore del trapezio"\]:::output --> E[/Input base minore/]:::input

    E --> F[\"Output: Inserisci l'altezza del trapezio"\]:::output --> G[/Input altezza/]:::input

    G --> H[\"Output: Inserisci il raggio del cerchio"\]:::output --> I[/Input raggio/]:::input

    I --> J["area_trapezio = (baseMaggiore + baseMinore) / 2 * altezza"]:::assign
    J --> K["area_cerchio = 3.14 * raggio * raggio"]:::assign

    K --> L{"area_trapezio = area_cerchio"}:::decision

    L -->|Sì| P[\"Output: Le aree delle due figure sono uguali"\]:::output

    L -->|No| L2{"area_trapezio > area_cerchio"}:::decision

    L2 -->|Sì| M[\"Output: L'area del trapezio è maggiore"\]:::output
    L2 -->|No| N[\"Output: L'area del cerchio è maggiore"\]:::output

    P --> O["Fine del programma"]:::startend
    M --> O["Fine del programma"]:::startend
    N --> O["Fine del programma"]:::startend
```

[Scarica il programma in formato Flowgorithm](./algoritmo_trapeziocerchio.fprg)

[Scarica il programma in formato Immagine (PNG)](./algoritmo_trapeziocerchio_img.png)

---

## 5. Schema delle variabili individuate

| Tipo | Variabili | Origine |
|------|-----------|---------|
| **Input** | baseMaggiore, baseMinore, altezza, raggio | esplicitati nel testo |
| **Elaborazione** | area_trapezio, area_cerchio | derivano dalle formule |
| **Output** | stessi valori delle aree + messaggio finale | richiesti dal problema |
| **Condizioni** | usa variabili esistenti | confronto tra aree |

---
