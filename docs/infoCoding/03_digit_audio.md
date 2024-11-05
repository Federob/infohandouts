# La Codifica dei Suoni: Campionamento e Frequenza di Campionamento

La **codifica dei suoni** è il processo con cui i suoni vengono digitalizzati, cioè trasformati in segnali che i computer possono memorizzare e processare. Poiché i suoni sono onde continue, è necessario "campionarli" per rappresentarli digitalmente.

## 1. Che cos'è il Campionamento?

Il **campionamento** è il processo con cui si misura l'ampiezza di un'onda sonora a intervalli regolari di tempo. Ogni misurazione è chiamata **campione**.

Immagina di voler rappresentare un'onda sonora, come quella della tua voce. Invece di registrarla come onda continua, la rappresentiamo come una serie di punti che indicano l'intensità del suono in momenti specifici.

### Esempio di Campionamento

Supponiamo di avere un'onda sonora molto semplice. Se prendiamo campioni dell'onda ogni millisecondo (ms), possiamo rappresentare l'onda sonora come una serie di valori numerici che descrivono l'intensità del suono in ogni millisecondo. Più campioni prendiamo, più precisa sarà la rappresentazione del suono.

## 2. La Frequenza di Campionamento

La **frequenza di campionamento** è il numero di campioni prelevati per secondo. Si misura in **Hertz (Hz)**, dove 1 Hz equivale a 1 campione al secondo. Frequenze di campionamento comuni includono:
- **8.000 Hz** – Usata nelle telefonate, con una qualità del suono ridotta.
- **44.100 Hz** – Usata per la qualità audio CD, che offre una buona fedeltà sonora.
- **48.000 Hz** – Usata per la qualità audio dei film e della TV.

Una frequenza di campionamento più alta significa che vengono presi più campioni per secondo, permettendo una riproduzione del suono più accurata.

### Esempio di Frequenza di Campionamento

Immagina di voler digitalizzare una nota musicale. Se la frequenza di campionamento è **8.000 Hz**, si prendono 8.000 campioni al secondo, mentre a **44.100 Hz**, si prendono 44.100 campioni al secondo. La seconda rappresentazione sarà più fedele al suono originale.

## 3. Risoluzione dei Campioni

Oltre alla frequenza di campionamento, anche la **risoluzione dei campioni** è importante. Essa indica il numero di bit utilizzati per rappresentare l’ampiezza di ciascun campione:
- **8 bit**: 256 valori possibili per ogni campione.
- **16 bit**: 65.536 valori possibili per ogni campione.

Più alta è la risoluzione, maggiore è la precisione con cui ogni campione rappresenta l'ampiezza dell'onda sonora.

### Esempio di Risoluzione

Un suono registrato con **8 bit** può sembrare "metallico" o "distorto" rispetto a uno registrato a **16 bit**, che avrà una qualità molto più naturale.

## 4. Rappresentazione Grafica del Campionamento

Un’onda sonora digitale può essere visualizzata come una serie di punti su un grafico, dove l’asse X rappresenta il tempo e l’asse Y rappresenta l’intensità del suono. 

### Diagrammi Riassuntivi

- **Campionamento di un’Onda Sonora** – Un’immagine che mostra come un’onda continua venga trasformata in una serie di campioni:
   - ![Esempio di Campionamento](https://upload.wikimedia.org/wikipedia/commons/2/29/Sampled_signal.png)
   
- **Frequenza di Campionamento** – Un’immagine che mostra la differenza tra una frequenza di campionamento bassa e una alta:
   - ![Frequenza di Campionamento](https://upload.wikimedia.org/wikipedia/commons/8/81/Sample.png)

## Conclusione

La qualità dell'audio digitale dipende principalmente dalla frequenza di campionamento e dalla risoluzione. Una frequenza di campionamento elevata e una risoluzione alta producono un audio più fedele all’originale, mentre una frequenza e una risoluzione basse portano a una qualità inferiore ma con minori requisiti di memoria.

### Esercizi

1. Quale sarà la qualità dell’audio se registrato a 8.000 Hz con una risoluzione di 8 bit? Per quale tipo di applicazione potrebbe essere adatta questa configurazione?
2. Trova la frequenza di campionamento minima per rappresentare un suono che ha una frequenza massima di 10.000 Hz (applica il **teorema di Nyquist**).
3. Spiega come la risoluzione dei campioni influenza la qualità audio.

