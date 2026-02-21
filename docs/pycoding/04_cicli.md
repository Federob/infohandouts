# Cicli

## Ripetere le operazioni

Spesso nei programmi devi **ripetere** un blocco di istruzioni più volte. Invece di scrivere lo stesso codice 100 volte, usi un **ciclo** (loop).

Python ha due tipi di ciclo:

- **`for`** - quando sai **quante volte** ripetere
- **`while`** - quando ripeti **finché** una condizione è vera

---

## Il ciclo `for`

### Ripetere N volte con `range()`

La funzione `range()` genera una sequenza di numeri:

```pyodide
# Ripete 5 volte (da 0 a 4)
for i in range(5):
    print(f"Ripetizione numero {i}")
```

### Varianti di `range()`

| Sintassi              | Genera                  | Esempio              |
|-----------------------|-------------------------|----------------------|
| `range(n)`            | Da 0 a n-1              | `range(5)` → 0,1,2,3,4 |
| `range(inizio, fine)` | Da inizio a fine-1      | `range(2, 6)` → 2,3,4,5 |
| `range(inizio, fine, passo)` | Con incremento   | `range(0, 10, 2)` → 0,2,4,6,8 |

```pyodide
# Da 1 a 10
print("Da 1 a 10:")
for i in range(1, 11):
    print(i, end=" ")

print()  # A capo

# Numeri pari da 0 a 20
print("\nNumeri pari da 0 a 20:")
for i in range(0, 21, 2):
    print(i, end=" ")

print()

# Conto alla rovescia
print("\nConto alla rovescia:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\nVia!")
```

### Iterare su una stringa

Il `for` può scorrere i caratteri di una stringa:

```pyodide
parola = "Python"

for carattere in parola:
    print(carattere)
```

---

## Il ciclo `while`

Il `while` ripete **finché la condizione è vera**:

```pyodide
contatore = 1

while contatore <= 5:
    print(f"Contatore: {contatore}")
    contatore += 1

print("Fine!")
```

!!! danger "Attenzione ai cicli infiniti!"

    Se la condizione del `while` non diventa mai falsa, il programma si blocca! Assicurati sempre che qualcosa cambi ad ogni iterazione.

    ```python
    # ERRORE: ciclo infinito!
    x = 1
    while x > 0:    # x sarà sempre > 0!
        print(x)
        x += 1      # x aumenta, non diminuisce mai
    ```

### Esempio: indovina il numero

```pyodide
import random

numero_segreto = random.randint(1, 20)
tentativi = 0

print("Indovina il numero (tra 1 e 20)!")

while True:
    tentativo = int(input("Il tuo tentativo: "))
    tentativi += 1

    if tentativo == numero_segreto:
        print(f"Bravo! Hai indovinato in {tentativi} tentativi!")
        break
    elif tentativo < numero_segreto:
        print("Troppo basso!")
    else:
        print("Troppo alto!")
```

---

## `break` e `continue`

Due istruzioni speciali per controllare il flusso di un ciclo:

### `break` - Esci dal ciclo

```pyodide
# Cerca il primo numero divisibile per 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Il primo multiplo di 7 è: {i}")
        break
```

### `continue` - Salta all'iterazione successiva

```pyodide
# Stampa solo i numeri dispari
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta i numeri pari
    print(i, end=" ")
```

---

## Cicli annidati

Puoi mettere un ciclo dentro un altro ciclo:

```pyodide
# Tabellina pitagorica (da 1 a 5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # A capo dopo ogni riga
```

### Esempio: disegnare un triangolo

```pyodide
altezza = 5

for i in range(1, altezza + 1):
    print("*" * i)
```

---

## Accumulatori e contatori

Due pattern fondamentali con i cicli:

### Contatore: contare quanti elementi soddisfano una condizione

```pyodide
frase = input("Scrivi una frase: ")

vocali = 0
for c in frase.lower():
    if c in "aeiou":
        vocali += 1

print(f"La frase contiene {vocali} vocali")
```

### Accumulatore: sommare valori

```pyodide
n = int(input("Quanti numeri vuoi sommare? "))
somma = 0

for i in range(n):
    numero = float(input(f"Numero {i+1}: "))
    somma += numero

media = somma / n
print(f"Somma: {somma}")
print(f"Media: {media:.2f}")
```

---

## `for` ... `else` e `while` ... `else`

In Python puoi aggiungere un `else` dopo un ciclo. Il blocco `else` viene eseguito solo se il ciclo termina **senza `break`**:

```pyodide
# Cerca un numero nella lista
numeri = [4, 8, 15, 16, 23, 42]
cerca = int(input("Che numero cerchi? "))

for n in numeri:
    if n == cerca:
        print(f"Trovato: {n}!")
        break
else:
    print(f"{cerca} non è presente nella lista")
```

---

## Esercizi

### Esercizio 1: Somma dei numeri

Calcola la somma dei numeri da 1 a N (dove N è inserito dall'utente).

```pyodide
n = int(input("Inserisci N: "))

# Calcola la somma da 1 a N

```

### Esercizio 2: Fattoriale

Calcola il fattoriale di un numero (es: 5! = 5 * 4 * 3 * 2 * 1 = 120).

```pyodide
n = int(input("Inserisci un numero: "))

# Calcola il fattoriale

```

### Esercizio 3: Numeri primi

Stampa tutti i numeri primi da 2 a N.

```pyodide
n = int(input("Inserisci N: "))

# Stampa i numeri primi fino a N

```
