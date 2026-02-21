# Condizioni

## Prendere decisioni

Fino ad ora i nostri programmi eseguivano tutte le istruzioni in sequenza, dall'alto verso il basso. Ma nella vita reale spesso dobbiamo **prendere decisioni**: "se piove prendo l'ombrello, altrimenti no".

In Python (come in Flowgorithm con il blocco rombo) si usano le istruzioni `if`, `elif` e `else`.

---

## L'istruzione `if`

La forma più semplice: **se** la condizione è vera, esegui il blocco di codice.

```pyodide
eta = int(input("Quanti anni hai? "))

if eta >= 18:
    print("Sei maggiorenne!")
    print("Puoi votare")
```

!!! warning "Indentazione obbligatoria!"

    Il codice dentro l'`if` **deve essere indentato** (spostato a destra di 4 spazi o 1 tab). Python usa l'indentazione per capire quali righe fanno parte del blocco. Non dimenticare i **due punti** `:` dopo la condizione!

---

## `if` ... `else`

Per gestire il caso "altrimenti":

```pyodide
eta = int(input("Quanti anni hai? "))

if eta >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")
```

---

## `if` ... `elif` ... `else`

Per gestire **più condizioni** in sequenza:

```pyodide
voto = int(input("Inserisci il voto (1-10): "))

if voto >= 9:
    print("Eccellente!")
elif voto >= 7:
    print("Buono")
elif voto >= 6:
    print("Sufficiente")
else:
    print("Insufficiente")
```

!!! tip "Come funziona?"

    Python controlla le condizioni **dall'alto verso il basso**. Appena ne trova una vera, esegue quel blocco e **salta tutte le altre**. Se nessuna è vera, esegue il blocco `else` (se presente).

---

## Operatori di confronto

Per scrivere le condizioni usi gli **operatori di confronto**:

| Operatore | Significato          | Esempio    | Risultato |
|-----------|----------------------|------------|-----------|
| `==`      | Uguale a             | `5 == 5`   | `True`    |
| `!=`      | Diverso da           | `5 != 3`   | `True`    |
| `>`       | Maggiore di          | `5 > 3`    | `True`    |
| `<`       | Minore di            | `5 < 3`    | `False`   |
| `>=`      | Maggiore o uguale    | `5 >= 5`   | `True`    |
| `<=`      | Minore o uguale      | `5 <= 3`   | `False`   |

```pyodide
x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x > 15)    # False
print(x <= 10)   # True
```

!!! danger "Errore classico: `=` vs `==`"

    - `=` è l'**assegnazione** (dai un valore a una variabile)
    - `==` è il **confronto** (verifichi se due valori sono uguali)

    ```python
    x = 5     # Assegna 5 a x
    x == 5    # Confronta: x è uguale a 5? (True)
    ```

---

## Operatori logici

Per combinare più condizioni, usa `and`, `or`, `not`:

| Operatore | Significato                         | Esempio                        |
|-----------|-------------------------------------|--------------------------------|
| `and`     | Vero se **entrambe** sono vere      | `x > 0 and x < 10`            |
| `or`      | Vero se **almeno una** è vera       | `x == 0 or x == 1`            |
| `not`     | Inverte il valore                   | `not (x > 5)`                 |

```pyodide
eta = int(input("Età: "))
patente = input("Hai la patente? (si/no): ")

if eta >= 18 and patente == "si":
    print("Puoi guidare!")
elif eta >= 18 and patente == "no":
    print("Puoi prendere la patente")
else:
    print("Sei troppo giovane per guidare")
```

### Tabella di verità

**AND** - entrambe devono essere vere:

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

**OR** - almeno una deve essere vera:

| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

```pyodide
# Verifica se un numero è in un intervallo
numero = int(input("Inserisci un numero: "))

if numero >= 1 and numero <= 10:
    print(f"{numero} è tra 1 e 10")
else:
    print(f"{numero} è fuori dall'intervallo 1-10")

# Verifica weekend
giorno = input("Che giorno è? ").lower()
if giorno == "sabato" or giorno == "domenica":
    print("È weekend!")
else:
    print("È un giorno lavorativo")
```

---

## Condizioni annidate

Puoi mettere un `if` dentro un altro `if`:

```pyodide
numero = int(input("Inserisci un numero: "))

if numero >= 0:
    if numero == 0:
        print("Il numero è zero")
    else:
        print("Il numero è positivo")
else:
    print("Il numero è negativo")
```

!!! tip "Quando annidare?"

    Le condizioni annidate funzionano, ma possono diventare difficili da leggere. Spesso è meglio usare `elif` o operatori logici per mantenere il codice piatto.

---

## Espressioni condizionali (operatore ternario)

Per condizioni semplici, puoi scrivere tutto in una riga:

```pyodide
eta = int(input("Età: "))

stato = "maggiorenne" if eta >= 18 else "minorenne"
print(f"Sei {stato}")
```

Questo equivale a:

```python
if eta >= 18:
    stato = "maggiorenne"
else:
    stato = "minorenne"
```

---

## Confronto tra stringhe

Anche le stringhe possono essere confrontate:

```pyodide
password_corretta = "python123"
tentativo = input("Inserisci la password: ")

if tentativo == password_corretta:
    print("Accesso consentito!")
else:
    print("Password sbagliata!")
```

---

## Esercizi

### Esercizio 1: Pari o dispari

Chiedi un numero all'utente e stampa se è pari o dispari (suggerimento: usa l'operatore `%`).

```pyodide
numero = int(input("Inserisci un numero: "))

# Verifica se è pari o dispari

```

### Esercizio 2: Calcolatrice

Chiedi due numeri e un operatore (+, -, *, /) e stampa il risultato.

```pyodide
n1 = float(input("Primo numero: "))
op = input("Operatore (+, -, *, /): ")
n2 = float(input("Secondo numero: "))

# Esegui l'operazione corretta in base all'operatore

```

### Esercizio 3: Voto in lettere

Converti un voto numerico (0-100) in una lettera: A (90-100), B (80-89), C (70-79), D (60-69), F (sotto 60).

```pyodide
voto = int(input("Inserisci il voto (0-100): "))

# Converti in lettera e stampa il risultato

```
