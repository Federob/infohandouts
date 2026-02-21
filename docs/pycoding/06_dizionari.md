# Dizionari e set

## Cos'è un dizionario?

Un dizionario è una collezione di coppie **chiave-valore**. Pensa a un dizionario vero: cerchi una **parola** (chiave) e trovi la sua **definizione** (valore).

```pyodide
# Dizionario: chiave → valore
studente = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 16,
    "media": 7.5
}

print(studente)
print(studente["nome"])
print(studente["media"])
```

---

## Creare un dizionario

```pyodide
# Dizionario vuoto
vuoto = {}

# Con valori iniziali
colori = {
    "rosso": "#FF0000",
    "verde": "#00FF00",
    "blu": "#0000FF"
}

# Con la funzione dict()
persona = dict(nome="Luigi", eta=20)

print(colori)
print(persona)
```

---

## Accesso e modifica

```pyodide
rubrica = {
    "Mario": "333-1234567",
    "Luigi": "333-7654321",
    "Peach": "333-1111111"
}

# Accesso
print(rubrica["Mario"])

# Modifica
rubrica["Mario"] = "333-9999999"
print("Mario aggiornato:", rubrica["Mario"])

# Aggiungere una nuova coppia
rubrica["Toad"] = "333-0000000"
print("Rubrica:", rubrica)
```

### Accesso sicuro con `get()`

```pyodide
rubrica = {"Mario": "333-1234567", "Luigi": "333-7654321"}

# Con [] se la chiave non esiste, dà errore
# print(rubrica["Peach"])  # KeyError!

# Con get() restituisce None (o un valore predefinito)
print(rubrica.get("Peach"))
print(rubrica.get("Peach", "Non trovato"))
print(rubrica.get("Mario", "Non trovato"))
```

---

## Rimuovere elementi

```pyodide
voti = {"matematica": 8, "italiano": 7, "inglese": 9, "storia": 6}

# Rimuovere con del
del voti["storia"]
print("Dopo del:", voti)

# Rimuovere con pop (restituisce il valore)
voto_inglese = voti.pop("inglese")
print(f"Inglese rimosso: {voto_inglese}")
print("Dopo pop:", voti)
```

---

## Iterare su un dizionario

```pyodide
voti = {"matematica": 8, "italiano": 7, "inglese": 9, "storia": 6}

# Iterare sulle chiavi
print("Materie:")
for materia in voti:
    print(f"  {materia}")

# Iterare sui valori
print("\nVoti:")
for voto in voti.values():
    print(f"  {voto}")

# Iterare su chiavi e valori insieme
print("\nPagella:")
for materia, voto in voti.items():
    print(f"  {materia}: {voto}")
```

---

## Metodi utili

```pyodide
persona = {"nome": "Mario", "eta": 16, "citta": "Roma"}

# Chiavi, valori, coppie
print("Chiavi:", list(persona.keys()))
print("Valori:", list(persona.values()))
print("Coppie:", list(persona.items()))

# Verifica se una chiave esiste
print("'nome' esiste?", "nome" in persona)
print("'peso' esiste?", "peso" in persona)

# Numero di coppie
print("Elementi:", len(persona))
```

---

## Dictionary comprehension

Come per le liste, puoi creare dizionari in modo compatto:

```pyodide
# Tabella dei quadrati
quadrati = {n: n**2 for n in range(1, 6)}
print(quadrati)

# Filtrare un dizionario
voti = {"matematica": 8, "italiano": 5, "inglese": 9, "storia": 4}
sufficienti = {m: v for m, v in voti.items() if v >= 6}
print("Sufficienti:", sufficienti)
```

---

## I Set

Un set è una **collezione non ordinata di elementi unici** (senza duplicati). Si crea con le parentesi graffe `{}`:

```pyodide
# Set: elimina automaticamente i duplicati
numeri = {1, 3, 5, 3, 7, 1, 9, 5}
print(numeri)  # I duplicati sono spariti!

# Creare un set da una lista
lista = [1, 2, 2, 3, 3, 3, 4]
insieme = set(lista)
print(insieme)
```

### Operazioni tra set

```pyodide
classe_a = {"Mario", "Luigi", "Peach", "Toad"}
classe_b = {"Luigi", "Yoshi", "Peach", "Daisy"}

# Unione: tutti gli studenti
print("Unione:", classe_a | classe_b)

# Intersezione: studenti in entrambe
print("In comune:", classe_a & classe_b)

# Differenza: solo in classe A
print("Solo A:", classe_a - classe_b)

# Differenza simmetrica: in una ma non nell'altra
print("Esclusivi:", classe_a ^ classe_b)
```

---

## Quando usare cosa?

| Struttura    | Uso tipico                               | Esempio                        |
|--------------|------------------------------------------|--------------------------------|
| **Lista**    | Collezione ordinata, con duplicati       | Voti di uno studente           |
| **Tupla**    | Dati fissi, non modificabili             | Coordinate (x, y)             |
| **Dizionario**| Associare chiavi a valori               | Rubrica, pagella               |
| **Set**      | Elementi unici, operazioni insiemistiche | Lista presenze senza duplicati |

---

## Esercizi

### Esercizio 1: Conta parole

Conta quante volte appare ogni parola in una frase.

```pyodide
frase = "il gatto e il cane e il pesce"
parole = frase.split()

# Crea un dizionario con il conteggio di ogni parola

```

### Esercizio 2: Rubrica

Crea una rubrica dove l'utente può aggiungere, cercare e visualizzare contatti.

```pyodide
rubrica = {}

# Aggiungi 3 contatti
for i in range(3):
    nome = input(f"Nome contatto {i+1}: ")
    tel = input(f"Telefono di {nome}: ")
    rubrica[nome] = tel

# Stampa la rubrica
print("\nRubrica completa:")
for nome, tel in rubrica.items():
    print(f"  {nome}: {tel}")
```
