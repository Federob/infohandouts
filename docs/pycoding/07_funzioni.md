# Funzioni

## Cos'è una funzione?

Una funzione è un **blocco di codice riutilizzabile** che svolge un compito specifico. Hai già usato funzioni predefinite come `print()`, `input()`, `len()`. Ora imparerai a creare le **tue** funzioni!

Perché usare le funzioni?

- **Riutilizzo**: scrivi il codice una volta, usalo quante volte vuoi
- **Organizzazione**: il programma è più leggibile
- **Manutenzione**: se devi correggere qualcosa, lo fai in un solo punto

---

## Definire una funzione

Si usa la parola chiave `def`:

```pyodide
# Definizione della funzione
def saluta():
    print("Ciao!")
    print("Benvenuto nel programma")

# Chiamata della funzione
saluta()
saluta()  # Puoi chiamarla quante volte vuoi!
```

!!! warning "Prima definisci, poi chiami!"

    La funzione deve essere **definita prima** di essere chiamata. Python legge il codice dall'alto verso il basso.

---

## Funzioni con parametri

I parametri permettono di passare dati alla funzione:

```pyodide
def saluta(nome):
    print(f"Ciao {nome}!")

saluta("Mario")
saluta("Luigi")
saluta("Peach")
```

### Più parametri

```pyodide
def presenta(nome, eta, citta):
    print(f"Mi chiamo {nome}, ho {eta} anni e vivo a {citta}")

presenta("Mario", 16, "Roma")
presenta("Luigi", 17, "Milano")
```

### Parametri con valore predefinito

```pyodide
def saluta(nome, lingua="italiano"):
    if lingua == "italiano":
        print(f"Ciao {nome}!")
    elif lingua == "inglese":
        print(f"Hello {nome}!")
    elif lingua == "spagnolo":
        print(f"Hola {nome}!")

saluta("Mario")                    # Usa il default: italiano
saluta("Mario", "inglese")         # Specifica la lingua
saluta("Mario", lingua="spagnolo") # Parametro nominato
```

---

## Il valore di ritorno (`return`)

Una funzione può **restituire un valore** con `return`:

```pyodide
def somma(a, b):
    risultato = a + b
    return risultato

# Il valore restituito può essere salvato in una variabile
s = somma(5, 3)
print(f"5 + 3 = {s}")

# Oppure usato direttamente
print(f"10 + 20 = {somma(10, 20)}")
```

### Restituire più valori

```pyodide
def analizza_numeri(lista):
    minimo = min(lista)
    massimo = max(lista)
    media = sum(lista) / len(lista)
    return minimo, massimo, media

numeri = [4, 8, 2, 9, 1, 7]
mi, ma, me = analizza_numeri(numeri)
print(f"Min: {mi}, Max: {ma}, Media: {me:.2f}")
```

!!! tip "return vs print"

    - `print()` **mostra** un valore sullo schermo, ma non lo "salva"
    - `return` **restituisce** un valore che può essere usato nel programma

    ```python
    def area_print(base, altezza):
        print(base * altezza)     # Mostra, ma non puoi riutilizzare il valore

    def area_return(base, altezza):
        return base * altezza     # Restituisce, puoi salvarlo e usarlo
    ```

---

## Scope delle variabili

Le variabili create dentro una funzione esistono **solo dentro quella funzione** (variabili locali):

```pyodide
def mia_funzione():
    x = 10  # Variabile locale
    print(f"Dentro la funzione: x = {x}")

mia_funzione()

# print(x)  # ERRORE! x non esiste fuori dalla funzione

# Le variabili esterne sono leggibili ma non modificabili
y = 100

def leggi_y():
    print(f"y vale: {y}")  # Può leggere y

leggi_y()
```

---

## Funzioni come strumenti

Esempio pratico: un insieme di funzioni per la geometria.

```pyodide
def area_rettangolo(base, altezza):
    return base * altezza

def area_triangolo(base, altezza):
    return base * altezza / 2

def area_cerchio(raggio):
    return 3.14159 * raggio ** 2

def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

# Uso delle funzioni
print("=== Calcolatrice Geometrica ===")
print(f"Rettangolo 5x3: area={area_rettangolo(5,3)}, perimetro={perimetro_rettangolo(5,3)}")
print(f"Triangolo base=6, h=4: area={area_triangolo(6,4)}")
print(f"Cerchio r=5: area={area_cerchio(5):.2f}")
```

---

## Funzioni ricorsive

Una funzione che **chiama se stessa**. Utile per problemi che si possono scomporre in sotto-problemi simili.

```pyodide
def fattoriale(n):
    if n <= 1:       # Caso base: ferma la ricorsione
        return 1
    else:
        return n * fattoriale(n - 1)  # Chiama se stessa

print(f"5! = {fattoriale(5)}")
print(f"10! = {fattoriale(10)}")
```

### Come funziona?

```
fattoriale(5)
= 5 * fattoriale(4)
= 5 * 4 * fattoriale(3)
= 5 * 4 * 3 * fattoriale(2)
= 5 * 4 * 3 * 2 * fattoriale(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

---

## Funzioni lambda

Per funzioni semplici di una sola riga, puoi usare le **lambda**:

```pyodide
# Funzione normale
def quadrato(x):
    return x ** 2

# Equivalente con lambda
quadrato_lambda = lambda x: x ** 2

print(quadrato(5))
print(quadrato_lambda(5))

# Utile con sort, map, filter
numeri = [3, 1, 4, 1, 5, 9]
numeri.sort(key=lambda x: -x)  # Ordina in modo decrescente
print("Ordinati (desc):", numeri)
```

---

## Esercizi

### Esercizio 1: Funzione massimo

Scrivi una funzione `massimo(a, b, c)` che restituisce il massimo tra tre numeri, senza usare la funzione `max()`.

```pyodide
def massimo(a, b, c):
    # Scrivi il codice qui
    pass

# Test
print(massimo(3, 7, 5))   # Deve stampare 7
print(massimo(10, 2, 8))  # Deve stampare 10
```

### Esercizio 2: Funzione palindroma

Scrivi una funzione che controlla se una parola è un palindromo (si legge uguale in entrambe le direzioni).

```pyodide
def is_palindroma(parola):
    # Scrivi il codice qui
    pass

# Test
print(is_palindroma("anna"))    # True
print(is_palindroma("ciao"))    # False
print(is_palindroma("radar"))   # True
```

### Esercizio 3: Fibonacci

Scrivi una funzione che restituisce l'n-esimo numero della sequenza di Fibonacci (1, 1, 2, 3, 5, 8, 13...).

```pyodide
def fibonacci(n):
    # Scrivi il codice qui
    pass

# Test: stampa i primi 10 numeri di Fibonacci
for i in range(1, 11):
    print(fibonacci(i), end=" ")
```
