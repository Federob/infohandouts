
# Dispensa HTML e CSS (base) - Primo anno Liceo Scientifico

## Cos'è HTML?
HTML (HyperText Markup Language) è il linguaggio che definisce il contenuto e la struttura delle pagine web, tramite **tag**.

### Struttura minima di una pagina HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Pagina HTML</title>
</head>
<body>
    <h1>Titolo pagina</h1>
    <p>Primo paragrafo della mia pagina web.</p>
</body>
</html>
```

## Tag HTML comuni con esempi

### Titoli e paragrafi

```html
<h1>Titolo grande</h1>
<h2>Titolo medio</h2>
<h3>Titolo piccolo</h3>

<p>Questo è un semplice paragrafo.</p>
```

### Testo formattato

```html
<b>Testo in grassetto</b><br>
<i>Testo in corsivo</i><br>
<u>Testo sottolineato</u>
```

### Immagine

```html
<img src="foto.jpg" alt="Descrizione della foto">
```

### Collegamento (link)

```html
<a href="https://www.wikipedia.org">Vai su Wikipedia</a>
```

### Liste

**Lista puntata:**

```html
<ul>
    <li>Primo elemento</li>
    <li>Secondo elemento</li>
</ul>
```

**Lista numerata:**

```html
<ol>
    <li>Primo elemento</li>
    <li>Secondo elemento</li>
</ol>
```

### Tabelle

```html
<table border="1">
    <tr>
        <th>Nome</th>
        <th>Età</th>
    </tr>
    <tr>
        <td>Luca</td>
        <td>15</td>
    </tr>
    <tr>
        <td>Anna</td>
        <td>16</td>
    </tr>
</table>
```

### Altri tag utili

```html
<br> <!-- per andare a capo -->
<hr> <!-- linea orizzontale -->
```

---

## CSS (base)

I CSS servono per personalizzare lo stile grafico della pagina web (colori, dimensioni, ecc.).

### Inserimento dei CSS in HTML

```html
<head>
    <style>
        h1 { color: red; }
        p { font-size: 16px; }
    </style>
</head>
```

### Esempi CSS semplici

**Testo e colori**

```css
h1 {
    color: blue;
    font-size: 30px;
}

p {
    color: black;
    font-size: 18px;
}
```

**Tabelle**

```css
table {
    width: 80%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
}

th {
    background-color: lightgray;
}
```

**Immagini**

```css
img {
    width: 250px;
    height: auto;
    border: 1px solid black;
}
```

---

## Esempio finale HTML + CSS

```html
<!DOCTYPE html>
<html>
<head>
    <title>Esempio HTML e CSS</title>
    <style>
        h1 { color: darkgreen; }
        p { font-size: 16px; }
        table { border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 5px; }
        th { background-color: yellow; }
    </style>
</head>
<body>
    <h1>La mia pagina</h1>
    <p>Questa pagina contiene vari elementi HTML e CSS.</p>

    <img src="immagine.jpg" alt="Foto di esempio">

    <p>Visita il sito <a href="https://www.google.it">Google</a>.</p>

    <table>
        <tr>
            <th>Materia</th>
            <th>Voto</th>
        </tr>
        <tr>
            <td>Matematica</td>
            <td>8</td>
        </tr>
        <tr>
            <td>Informatica</td>
            <td>9</td>
        </tr>
    </table>

</body>
</html>
```

---

Ora prova tu a creare una pagina simile sul tuo computer!

Buon lavoro!
