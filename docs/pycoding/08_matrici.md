# Array e matrici

## Liste come array

Python non ha un tipo "array" nativo come altri linguaggi, ma le **liste** funzionano allo stesso modo. Una lista di numeri è un array a tutti gli effetti.

```pyodide
# Array di numeri
temperature = [22.5, 24.0, 19.8, 21.3, 25.1, 23.7, 20.5]

print("Temperature della settimana:", temperature)
print("Lunedì:", temperature[0])
print("Domenica:", temperature[6])
print("Media:", sum(temperature) / len(temperature))
```

---

## Operazioni tipiche sugli array

### Ricerca del massimo e minimo (manuale)

```pyodide
numeri = [34, 12, 67, 45, 89, 23, 56]

# Trova il massimo manualmente
massimo = numeri[0]
for n in numeri:
    if n > massimo:
        massimo = n

print(f"Massimo: {massimo}")

# Trova il minimo manualmente
minimo = numeri[0]
for n in numeri:
    if n < minimo:
        minimo = n

print(f"Minimo: {minimo}")
```

### Ricerca lineare

```pyodide
def cerca(lista, valore):
    for i in range(len(lista)):
        if lista[i] == valore:
            return i  # Restituisce la posizione
    return -1  # Non trovato

numeri = [10, 25, 30, 45, 50, 65, 70]

pos = cerca(numeri, 45)
if pos >= 0:
    print(f"45 trovato alla posizione {pos}")
else:
    print("45 non trovato")
```

### Ordinamento (Bubble Sort)

```pyodide
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

numeri = [64, 34, 25, 12, 22, 11, 90]
print("Prima:", numeri)

bubble_sort(numeri)
print("Dopo:", numeri)
```

---

## Matrici (liste di liste)

Una **matrice** è una tabella di numeri organizzata in righe e colonne. In Python si rappresenta come una **lista di liste**:

```pyodide
# Matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accesso: matrice[riga][colonna]
print("Elemento [0][0]:", matrice[0][0])  # 1
print("Elemento [1][2]:", matrice[1][2])  # 6
print("Elemento [2][1]:", matrice[2][1])  # 8
```

### Visualizzare una matrice

```pyodide
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Stampa formattata
for riga in matrice:
    for elemento in riga:
        print(f"{elemento:4}", end="")
    print()
```

---

## Creare matrici

### Matrice di zeri

```pyodide
righe = 3
colonne = 4

# Matrice 3x4 di zeri
matrice = []
for i in range(righe):
    riga = []
    for j in range(colonne):
        riga.append(0)
    matrice.append(riga)

# Stampa
for riga in matrice:
    print(riga)
```

### Con list comprehension

```pyodide
righe = 3
colonne = 4

# Matrice di zeri (compatta)
matrice = [[0 for j in range(colonne)] for i in range(righe)]

for riga in matrice:
    print(riga)

print()

# Matrice identità 4x4
identita = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

for riga in identita:
    print(riga)
```

---

## Operazioni sulle matrici

### Somma di due matrici

```pyodide
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

righe = len(A)
colonne = len(A[0])

# Matrice risultato
C = [[0 for j in range(colonne)] for i in range(righe)]

for i in range(righe):
    for j in range(colonne):
        C[i][j] = A[i][j] + B[i][j]

print("A + B =")
for riga in C:
    print(riga)
```

### Trasposta di una matrice

```pyodide
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

righe = len(matrice)
colonne = len(matrice[0])

# La trasposta scambia righe e colonne
trasposta = [[0 for j in range(righe)] for i in range(colonne)]

for i in range(righe):
    for j in range(colonne):
        trasposta[j][i] = matrice[i][j]

print("Originale:")
for riga in matrice:
    print(riga)

print("\nTrasposta:")
for riga in trasposta:
    print(riga)
```

### Somma per righe e colonne

```pyodide
voti = [
    [8, 7, 9],  # Studente 1
    [6, 8, 7],  # Studente 2
    [9, 9, 10], # Studente 3
]
materie = ["Mate", "Ita", "Ing"]

# Media per studente (per riga)
print("Medie per studente:")
for i, riga in enumerate(voti):
    media = sum(riga) / len(riga)
    print(f"  Studente {i+1}: {media:.2f}")

# Media per materia (per colonna)
print("\nMedie per materia:")
for j in range(len(materie)):
    somma = 0
    for i in range(len(voti)):
        somma += voti[i][j]
    media = somma / len(voti)
    print(f"  {materie[j]}: {media:.2f}")
```

---

## Esempio pratico: griglia di gioco

```pyodide
# Inizializza griglia 3x3 (tris)
griglia = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

# Stampa la griglia
print("  0 1 2")
for i, riga in enumerate(griglia):
    print(f"{i} {' '.join(riga)}")

# Controlla se X ha vinto (diagonale principale)
if griglia[0][0] == griglia[1][1] == griglia[2][2]:
    print(f"\n{griglia[0][0]} ha vinto sulla diagonale!")
```

---

## Esercizi

### Esercizio 1: Somma diagonale

Calcola la somma degli elementi sulla diagonale principale di una matrice quadrata.

```pyodide
matrice = [
    [5, 2, 3],
    [1, 8, 6],
    [4, 7, 9]
]

# Calcola la somma della diagonale principale (5 + 8 + 9 = 22)

```

### Esercizio 2: Matrice moltiplicata per scalare

Moltiplica tutti gli elementi di una matrice per un numero.

```pyodide
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
scalare = 3

# Moltiplica ogni elemento per lo scalare e stampa il risultato

```

### Esercizio 3: Cerca nella matrice

Cerca un valore in una matrice e restituisci la sua posizione (riga, colonna).

```pyodide
matrice = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

valore = int(input("Che numero cerchi? "))

# Cerca il valore e stampa la posizione

```
