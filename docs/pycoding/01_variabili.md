# Variabili, tipi di dati e operatori

## Cos'è una variabile?

Una variabile è un **contenitore con un nome** che conserva un valore in memoria. Puoi pensarla come una scatola con un'etichetta.

In Python, crei una variabile semplicemente assegnandole un valore con `=`:

```pyodide
nome = "Mario"
eta = 16
altezza = 1.75

print(nome)
print(eta)
print(altezza)
```

!!! tip "Nessuna dichiarazione!"

    A differenza di Flowgorithm (dove devi fare `Declare Integer x`), in Python **non serve dichiarare il tipo**. Python lo capisce da solo dal valore che assegni!

---

## I tipi di dati fondamentali

Python ha 4 tipi di dati di base:

| Tipo      | Nome Python | Esempio         | Descrizione                 |
|-----------|-------------|-----------------|-----------------------------|
| Intero    | `int`       | `42`, `-7`, `0` | Numeri senza virgola        |
| Decimale  | `float`     | `3.14`, `-0.5`  | Numeri con virgola (punto!) |
| Stringa   | `str`       | `"ciao"`, `'ok'`| Testo tra virgolette        |
| Booleano  | `bool`      | `True`, `False` | Vero o Falso                |

```pyodide
# Verifica i tipi con la funzione type()
intero = 42
decimale = 3.14
testo = "ciao"
booleano = True

print(type(intero))
print(type(decimale))
print(type(testo))
print(type(booleano))
```

---

## Regole per i nomi delle variabili

Non puoi dare un nome qualsiasi alle variabili. Ecco le regole:

- **Possono contenere**: lettere, numeri e underscore `_`
- **Devono iniziare** con una lettera o underscore (mai con un numero)
- **Sono case-sensitive**: `nome` e `Nome` sono variabili diverse!
- **Non possono** essere parole riservate di Python (`if`, `for`, `print`...)

| Nome         | Valido? | Perché                            |
|--------------|---------|-----------------------------------|
| `eta`        | Si      | Solo lettere                      |
| `nome_utente`| Si      | Lettere e underscore              |
| `x1`         | Si      | Lettera seguita da numero         |
| `1nome`      | No      | Inizia con un numero              |
| `nome utente`| No      | Contiene uno spazio               |
| `for`        | No      | Parola riservata di Python        |

!!! tip "Convenzione Python"

    In Python si usa lo **snake_case** per i nomi delle variabili: parole minuscole separate da underscore. Esempio: `area_rettangolo`, `base_maggiore`, `nome_utente`.

---

## Operatori aritmetici

Gli operatori permettono di fare calcoli con i numeri:

| Operatore | Significato        | Esempio    | Risultato |
|-----------|--------------------|------------|-----------|
| `+`       | Addizione          | `5 + 3`    | `8`       |
| `-`       | Sottrazione        | `5 - 3`    | `2`       |
| `*`       | Moltiplicazione    | `5 * 3`    | `15`      |
| `/`       | Divisione          | `5 / 2`    | `2.5`     |
| `//`      | Divisione intera   | `5 // 2`   | `2`       |
| `%`       | Resto (modulo)     | `5 % 2`    | `1`       |
| `**`      | Potenza            | `5 ** 2`   | `25`      |

```pyodide
a = 17
b = 5

print("Addizione:", a + b)
print("Sottrazione:", a - b)
print("Moltiplicazione:", a * b)
print("Divisione:", a / b)
print("Divisione intera:", a // b)
print("Resto:", a % b)
print("Potenza:", a ** b)
```

### Precedenza degli operatori

Come in matematica, le operazioni hanno una **precedenza**:

1. `**` (potenza) - si esegue per prima
2. `*`, `/`, `//`, `%` (moltiplicazione, divisione, resto)
3. `+`, `-` (addizione, sottrazione)

Usa le **parentesi** `()` per forzare l'ordine:

```pyodide
# Senza parentesi: prima * poi +
risultato1 = 2 + 3 * 4
print("2 + 3 * 4 =", risultato1)

# Con parentesi: prima + poi *
risultato2 = (2 + 3) * 4
print("(2 + 3) * 4 =", risultato2)
```

---

## Conversione dei tipi (casting)

Spesso devi **convertire** un valore da un tipo all'altro. Le funzioni principali sono:

| Funzione   | Converte in | Esempio                    |
|------------|-------------|----------------------------|
| `int()`    | Intero      | `int("42")` → `42`        |
| `float()`  | Decimale    | `float("3.14")` → `3.14`  |
| `str()`    | Stringa     | `str(42)` → `"42"`        |
| `bool()`   | Booleano    | `bool(1)` → `True`        |

```pyodide
# Conversione stringa → numero
testo = "100"
numero = int(testo)
print(numero + 50)  # Ora puoi fare calcoli!

# Conversione numero → stringa
eta = 16
messaggio = "Ho " + str(eta) + " anni"
print(messaggio)
```

### Input e conversione

Ricorda: `input()` restituisce **sempre una stringa**! Per fare calcoli devi convertire:

```pyodide
# CORRETTO: converto in int prima di calcolare
numero = int(input("Scrivi un numero: "))
doppio = numero * 2
print("Il doppio è:", doppio)
```

---

## Operatori di assegnazione composti

Python offre delle scorciatoie per modificare una variabile:

| Operatore | Equivale a       | Esempio               |
|-----------|-------------------|-----------------------|
| `+=`      | `x = x + valore`  | `x += 3` (aggiunge 3) |
| `-=`      | `x = x - valore`  | `x -= 3` (toglie 3)   |
| `*=`      | `x = x * valore`  | `x *= 2` (raddoppia)  |
| `/=`      | `x = x / valore`  | `x /= 2` (dimezza)    |

```pyodide
punti = 100
print("Punti iniziali:", punti)

punti += 50  # Guadagno 50 punti
print("Dopo bonus:", punti)

punti -= 30  # Perdo 30 punti
print("Dopo penalità:", punti)

punti *= 2   # Raddoppio
print("Dopo moltiplicatore:", punti)
```

---

## Esercizi

### Esercizio 1: Conversione temperatura

Scrivi un programma che converta una temperatura da Celsius a Fahrenheit. Formula: `F = C * 1.8 + 32`

```pyodide
# Completa il programma!
celsius = float(input("Temperatura in Celsius: "))

# Scrivi la formula qui sotto


# Stampa il risultato

```

### Esercizio 2: Calcolo sconto

Un prodotto costa 80 euro e ha uno sconto del 15%. Calcola il prezzo scontato.

```pyodide
prezzo = 80
sconto_percentuale = 15

# Calcola lo sconto e il prezzo finale


# Stampa il risultato

```
