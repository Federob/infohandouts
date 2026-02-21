# Liste e tuple

## Cos'è una lista?

Una lista è una **collezione ordinata di elementi**. Puoi pensarla come un contenitore che tiene più valori insieme, ognuno accessibile tramite un indice.

```pyodide
# Lista di numeri
voti = [8, 7, 9, 6, 8, 10]
print(voti)

# Lista di stringhe
nomi = ["Mario", "Luigi", "Peach"]
print(nomi)

# Lista mista (sconsigliata ma possibile)
mista = [42, "ciao", True, 3.14]
print(mista)

# Lista vuota
vuota = []
print(vuota)
```

---

## Accesso agli elementi

Come per le stringhe, gli indici partono da **0**:

```pyodide
frutta = ["mela", "banana", "arancia", "kiwi", "pera"]

print(frutta[0])    # Primo: mela
print(frutta[2])    # Terzo: arancia
print(frutta[-1])   # Ultimo: pera
print(frutta[-2])   # Penultimo: kiwi
```

### Slicing (sotto-liste)

```pyodide
numeri = [10, 20, 30, 40, 50, 60, 70]

print(numeri[1:4])    # [20, 30, 40]
print(numeri[:3])     # [10, 20, 30]
print(numeri[4:])     # [50, 60, 70]
print(numeri[::2])    # [10, 30, 50, 70] (ogni 2)
print(numeri[::-1])   # [70, 60, 50, 40, 30, 20, 10] (invertita)
```

---

## Modificare una lista

A differenza delle stringhe, le liste **sono mutabili**: puoi cambiare i loro elementi.

```pyodide
colori = ["rosso", "verde", "blu"]
print("Prima:", colori)

# Modificare un elemento
colori[1] = "giallo"
print("Dopo modifica:", colori)

# Aggiungere in fondo
colori.append("viola")
print("Dopo append:", colori)

# Inserire in una posizione specifica
colori.insert(1, "arancione")
print("Dopo insert:", colori)
```

---

## Rimuovere elementi

```pyodide
animali = ["gatto", "cane", "pesce", "coniglio", "cane"]

# Rimuovere per valore (solo la prima occorrenza)
animali.remove("cane")
print("Dopo remove:", animali)

# Rimuovere per indice
rimosso = animali.pop(1)  # Rimuove e restituisce l'elemento
print(f"Rimosso: {rimosso}")
print("Dopo pop:", animali)

# Rimuovere l'ultimo elemento
ultimo = animali.pop()
print(f"Ultimo rimosso: {ultimo}")
print("Lista finale:", animali)
```

---

## Operazioni sulle liste

```pyodide
numeri = [3, 1, 4, 1, 5, 9, 2, 6]

print("Lunghezza:", len(numeri))
print("Somma:", sum(numeri))
print("Minimo:", min(numeri))
print("Massimo:", max(numeri))

# Ordinamento
numeri.sort()
print("Ordinata:", numeri)

numeri.sort(reverse=True)
print("Ordine inverso:", numeri)

# Contare occorrenze
print("Quanti 1:", numeri.count(1))

# Verificare appartenenza
print("5 è presente?", 5 in numeri)
print("7 è presente?", 7 in numeri)
```

---

## Iterare sulle liste

### Con `for`

```pyodide
frutta = ["mela", "banana", "arancia"]

# Modo semplice
for f in frutta:
    print(f"Mi piace la {f}")
```

### Con `enumerate()` (indice + valore)

```pyodide
frutta = ["mela", "banana", "arancia"]

for i, f in enumerate(frutta):
    print(f"{i}: {f}")
```

---

## List comprehension

Un modo compatto per creare liste:

```pyodide
# Modo classico
quadrati = []
for i in range(1, 6):
    quadrati.append(i ** 2)
print("Classico:", quadrati)

# List comprehension (stessa cosa, una riga!)
quadrati = [i ** 2 for i in range(1, 6)]
print("Comprehension:", quadrati)

# Con condizione: solo numeri pari
pari = [i for i in range(1, 21) if i % 2 == 0]
print("Pari:", pari)
```

---

## Le tuple

Una tupla è come una lista, ma **immutabile**: non puoi modificarla dopo la creazione. Si usa con le parentesi tonde `()`:

```pyodide
# Tupla
coordinate = (10, 20)
print(coordinate)
print(coordinate[0])
print(coordinate[1])

# Provare a modificare causa errore:
# coordinate[0] = 30  # TypeError!

# Unpacking: estrarre i valori
x, y = coordinate
print(f"x = {x}, y = {y}")
```

### Quando usare tuple vs liste?

| Caratteristica | Lista `[]`             | Tupla `()`               |
|----------------|------------------------|--------------------------|
| Mutabile       | Si                     | No                       |
| Uso tipico     | Collezione che cambia  | Dati fissi, coordinate   |
| Performance    | Leggermente più lenta  | Leggermente più veloce   |

```pyodide
# La tupla è perfetta per dati che non devono cambiare
giorni_settimana = ("lun", "mar", "mer", "gio", "ven", "sab", "dom")
print(giorni_settimana)

# Funzione che restituisce più valori (usa una tupla)
def min_max(lista):
    return min(lista), max(lista)

numeri = [4, 2, 7, 1, 9, 3]
minimo, massimo = min_max(numeri)
print(f"Min: {minimo}, Max: {massimo}")
```

---

## Esercizi

### Esercizio 1: Media voti

Chiedi all'utente 5 voti, salvali in una lista e calcola la media.

```pyodide
voti = []

# Chiedi 5 voti e aggiungili alla lista

# Calcola e stampa la media

```

### Esercizio 2: Lista senza duplicati

Data una lista, crea una nuova lista senza elementi duplicati.

```pyodide
numeri = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crea una lista senza duplicati

```

### Esercizio 3: Inversione lista

Inverti una lista senza usare il metodo `reverse()` o lo slicing `[::-1]`.

```pyodide
originale = [10, 20, 30, 40, 50]

# Inverti la lista manualmente con un ciclo

```
