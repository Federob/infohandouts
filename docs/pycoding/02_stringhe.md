# Stringhe

## Cos'è una stringa?

Una stringa è una **sequenza di caratteri** (testo). In Python si crea racchiudendo il testo tra virgolette doppie `"..."` o singole `'...'`:

```pyodide
saluto = "Ciao mondo"
nome = 'Mario'

print(saluto)
print(nome)
```

Per testo su **più righe**, usa le triple virgolette `"""..."""`:

```pyodide
poesia = """Sempre caro mi fu quest'ermo colle,
e questa siepe, che da tanta parte
dell'ultimo orizzonte il guardo esclude."""

print(poesia)
```

---

## Lunghezza di una stringa

La funzione `len()` restituisce il **numero di caratteri** (inclusi gli spazi):

```pyodide
parola = "Python"
print(len(parola))  # 6

frase = "Ciao mondo"
print(len(frase))   # 10 (lo spazio conta!)
```

---

## Accesso ai singoli caratteri

Ogni carattere ha una **posizione** (indice) che parte da **0**:

```
 P   y   t   h   o   n
[0] [1] [2] [3] [4] [5]
```

```pyodide
parola = "Python"

print(parola[0])   # Primo carattere: P
print(parola[1])   # Secondo carattere: y
print(parola[5])   # Ultimo carattere: n
print(parola[-1])  # Ultimo carattere (dal fondo): n
print(parola[-2])  # Penultimo: o
```

!!! tip "Indici negativi"

    Gli indici negativi contano **dalla fine**: `-1` è l'ultimo carattere, `-2` il penultimo, ecc.

---

## Slicing (sottostringhe)

Puoi estrarre una **porzione** della stringa con la sintassi `[inizio:fine]`:

```pyodide
parola = "Python"

print(parola[0:3])   # Pyt (da indice 0 a 2, il 3 è escluso!)
print(parola[2:5])   # tho
print(parola[:3])    # Pyt (dall'inizio fino a 2)
print(parola[3:])    # hon (da 3 fino alla fine)
print(parola[:])     # Python (tutta la stringa)
```

!!! warning "Il secondo indice è escluso!"

    `parola[0:3]` prende i caratteri alle posizioni 0, 1, 2 ma **NON** il 3.

---

## Concatenazione e ripetizione

```pyodide
# Concatenazione: unire stringhe con +
nome = "Mario"
cognome = "Rossi"
nome_completo = nome + " " + cognome
print(nome_completo)

# Ripetizione: ripetere una stringa con *
linea = "-" * 30
print(linea)
print("TITOLO")
print(linea)
```

!!! warning "Attenzione ai tipi!"

    Non puoi concatenare una stringa con un numero direttamente. Devi convertire il numero con `str()`:

    ```python
    eta = 16
    # print("Ho " + eta + " anni")       # ERRORE!
    print("Ho " + str(eta) + " anni")     # OK
    ```

---

## Metodi delle stringhe

Le stringhe hanno molti **metodi** (funzioni integrate). Ecco i più utili:

### Maiuscole e minuscole

```pyodide
testo = "ciao Mondo"

print(testo.upper())       # CIAO MONDO
print(testo.lower())       # ciao mondo
print(testo.capitalize())  # Ciao mondo
print(testo.title())       # Ciao Mondo
print(testo.swapcase())    # CIAO mONDO
```

### Ricerca

```pyodide
frase = "Python è un linguaggio fantastico"

# Cercare se contiene una sotto-stringa
print("Python" in frase)      # True
print("Java" in frase)        # False

# Trovare la posizione
print(frase.find("linguaggio"))   # 14 (indice dove inizia)
print(frase.find("Java"))         # -1 (non trovato)

# Contare le occorrenze
print(frase.count("a"))           # 3
```

### Sostituzione

```pyodide
frase = "Mi piace la pizza"

nuova = frase.replace("pizza", "pasta")
print(nuova)

# Puoi concatenare più sostituzioni
testo = "uno-due-tre"
risultato = testo.replace("-", " ")
print(risultato)
```

### Rimozione spazi

```pyodide
testo = "   ciao mondo   "

print(repr(testo.strip()))    # 'ciao mondo' (rimuove spazi da entrambi i lati)
print(repr(testo.lstrip()))   # 'ciao mondo   ' (solo a sinistra)
print(repr(testo.rstrip()))   # '   ciao mondo' (solo a destra)
```

### Split e Join

```pyodide
# Split: divide una stringa in una lista
frase = "uno,due,tre,quattro"
parti = frase.split(",")
print(parti)

# Join: unisce una lista in una stringa
parole = ["Ciao", "a", "tutti"]
frase = " ".join(parole)
print(frase)
```

---

## F-string (formattazione moderna)

Le **f-string** sono il modo più comodo per inserire variabili dentro una stringa. Basta mettere una `f` prima delle virgolette:

```pyodide
nome = "Mario"
eta = 16
media = 7.856

# F-string base
print(f"Mi chiamo {nome} e ho {eta} anni")

# Espressioni dentro le parentesi graffe
print(f"L'anno prossimo avrò {eta + 1} anni")

# Formattazione numeri decimali
print(f"La mia media è {media:.2f}")  # 2 cifre decimali
print(f"La mia media è {media:.1f}")  # 1 cifra decimale
```

### Formattazione avanzata con f-string

```pyodide
# Allineamento
for i in range(1, 6):
    print(f"Riga {i:>3} | {'*' * i:<10} |")

# Riempimento con zeri
numero = 42
print(f"Codice: {numero:05d}")  # 00042
```

---

## Caratteri speciali

Alcuni caratteri speciali si scrivono con il **backslash** `\`:

| Sequenza | Significato       |
|----------|-------------------|
| `\n`     | A capo            |
| `\t`     | Tabulazione       |
| `\\`     | Backslash         |
| `\"`     | Virgolette doppie |
| `\'`     | Virgolette singole |

```pyodide
print("Prima riga\nSeconda riga")
print("Colonna1\tColonna2\tColonna3")
print("Lui disse: \"Ciao!\"")
```

---

## Le stringhe sono immutabili

In Python le stringhe **non possono essere modificate** dopo la creazione. Per "modificarle" devi creare una nuova stringa:

```pyodide
parola = "Ciao"

# parola[0] = "M"  # ERRORE! Le stringhe sono immutabili

# Per "modificare", crea una nuova stringa:
nuova_parola = "M" + parola[1:]
print(nuova_parola)  # Miao
```

---

## Esercizi

### Esercizio 1: Analisi stringa

Chiedi una parola all'utente e stampa: la lunghezza, il primo e l'ultimo carattere, la parola in maiuscolo.

```pyodide
parola = input("Scrivi una parola: ")

# Completa qui sotto

```

### Esercizio 2: Inverti stringa

Stampa una parola al contrario (suggerimento: usa lo slicing con passo negativo `[::-1]`).

```pyodide
parola = input("Scrivi una parola: ")

# Inverti la parola e stampala

```

### Esercizio 3: Conta vocali

Conta quante vocali ci sono in una frase.

```pyodide
frase = input("Scrivi una frase: ").lower()
vocali = 0

# Conta le vocali (a, e, i, o, u) nella frase

```
