# Introduzione a Python

## Cos'è Python?

Python è un **linguaggio di programmazione** creato da Guido van Rossum nel 1991. È uno dei linguaggi più usati al mondo, sia da chi inizia sia dai professionisti.

Perché è così popolare?

- **Sintassi semplice e leggibile**: sembra quasi di scrivere in inglese
- **Versatile**: si usa per web, intelligenza artificiale, analisi dati, automazione e molto altro
- **Enorme community**: trovi risposte a qualsiasi domanda online

!!! tip "Editor interattivo"

    In queste pagine troverai degli **editor Python interattivi**: puoi modificare il codice e premere **Run** (o `Ctrl+Enter`) per eseguirlo direttamente nel browser, senza installare nulla!

---

## Il tuo primo programma

Tradizionalmente, il primo programma che si scrive in qualsiasi linguaggio è "Hello World". In Python è semplicissimo:

```pyodide
print("Hello World!")
```

Prova a modificare il messaggio e clicca **Run**!

---

## La funzione `print()`

`print()` è la funzione che **mostra un messaggio** sullo schermo (l'equivalente del blocco Output di Flowgorithm).

```pyodide
print("Ciao!")
print("Mi chiamo Python")
print("2 + 3 =", 2 + 3)
```

Puoi stampare:

- **Testo** (tra virgolette `"..."` o apici `'...'`)
- **Numeri** (senza virgolette)
- **Più cose insieme**, separate da virgole

---

## La funzione `input()`

`input()` **chiede un dato all'utente** (l'equivalente del blocco Input di Flowgorithm).

```pyodide
nome = input("Come ti chiami? ")
print("Ciao", nome, "!")
```

!!! warning "Attenzione"

    `input()` restituisce **sempre una stringa** (testo), anche se l'utente scrive un numero. Per fare calcoli, devi **convertire** il valore. Lo vedremo nella prossima sezione!

---

## Commenti

I commenti servono a **spiegare il codice** a chi lo legge (incluso il te stesso del futuro!). Python li ignora completamente durante l'esecuzione.

```pyodide
# Questo è un commento: Python lo ignora
print("Questa riga viene eseguita")  # Commento a fine riga

# I commenti aiutano a organizzare il codice:
# ======== INPUT ========
nome = input("Il tuo nome: ")

# ======== OUTPUT ========
print("Benvenuto,", nome)
```

---

## Struttura di un programma Python

Un programma Python si legge **dall'alto verso il basso**, riga per riga. Non c'è bisogno di dichiarare "Inizio" e "Fine" come in Flowgorithm.

La struttura tipica segue sempre lo schema:

```python
# 1. INPUT - Raccolta dati
# 2. ELABORAZIONE - Calcoli e operazioni
# 3. OUTPUT - Mostra i risultati
```

**Esempio completo:**

```pyodide
# Programma che calcola l'area di un rettangolo

# INPUT
base = float(input("Inserisci la base: "))
altezza = float(input("Inserisci l'altezza: "))

# ELABORAZIONE
area = base * altezza

# OUTPUT
print("L'area del rettangolo è:", area)
```

---

## Come eseguire Python sul tuo computer

Oltre all'editor interattivo di queste pagine, puoi eseguire Python sul tuo computer:

### Installazione

1. Scarica Python da [python.org](https://www.python.org/downloads/)
2. Durante l'installazione, **spunta "Add Python to PATH"**
3. Installa

### Editor consigliati

- **IDLE** - incluso con Python, semplice per iniziare
- **Visual Studio Code** - professionale, gratuito
- **PyCharm Community** - completo, ottimo per progetti

### Esecuzione

1. Crea un file con estensione `.py` (esempio: `programma.py`)
2. Scrivi il codice
3. Apri il terminale e digita: `python programma.py`
