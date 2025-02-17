# Interfaccia da linea di comando (CLI)

Questo documento descrive come navigare, creare, modificare e cancellare file e cartelle usando la riga di comando in Windows e Linux. Vengono presentati esempi realistici con prompt, comandi e output simulati, che mostrano il comportamento di un sistema operativo reale.

---

## 1. Introduzione alla CLI

La Command Line Interface (CLI) consente di eseguire comandi testuali per interagire direttamente con il sistema operativo.

• In Windows si accede tramite il Prompt dei comandi o PowerShell.  
• In Linux si utilizza il Terminale (con shell come bash o zsh).

Esempio simulato in Windows:

    C:\Users\User> echo Welcome to the Windows CLI!  
    Welcome to the Windows CLI!

Esempio simulato in Linux:

    user@ubuntu:~$ echo "Welcome to the Linux CLI!"  
    Welcome to the Linux CLI!

---

## 2. Navigare e visualizzare contenuti

### 2.1 Navigazione in Windows

Per spostarsi in una cartella si usa il comando cd.

Esempio:

    C:\Users\User> cd Desktop  
    C:\Users\User\Desktop>

Per elencare il contenuto della directory si usa il comando dir.

Esempio:

    C:\Users\User\Desktop> dir  
    Volume in drive C has no label.  
    Volume Serial Number is XXXX-XXXX  
    Directory of C:\Users\User\Desktop  
    01/01/2021  10:00 AM    <DIR>         .  
    01/01/2021  10:00 AM    <DIR>         ..  
    01/01/2021  10:05 AM             1,024 sample.txt  
                       1 File(s)          1,024 bytes  
                       2 Dir(s)  100,000,000,000 bytes free

### 2.2 Navigazione in Linux

Per spostarsi in una directory:

    user@ubuntu:~$ cd /home/user/Desktop  
    user@ubuntu:~/Desktop$

Per elencare i file:

    user@ubuntu:~/Desktop$ ls  
    Documenti  Immagini  Progetti

Per una visualizzazione dettagliata:

    user@ubuntu:~/Desktop$ ls -l  
    total 8  
    drwxr-xr-x 2 user user 4096 Jan  1 10:00 Documenti  
    drwxr-xr-x 2 user user 4096 Jan  1 10:05 Immagini  
    drwxr-xr-x 2 user user 4096 Jan  1 10:10 Progetti

---

## 3. Creazione di file e cartelle

### 3.1 In Windows

**Creare una cartella:**

    C:\Users\User> mkdir NuovaCartella

**Creare un file vuoto:**

    C:\Users\User> type nul > file_vuoto.txt  
    (Oppure: C:\Users\User> fsutil file createnew file_vuoto.txt 0)

**Creare un file e scriverci del testo:**

- Metodo "copy con":  
        C:\Users\User> copy con testo.txt  
        (Digitare: "Questo è un esempio di testo." e premere Ctrl+Z, poi Invio)  
        Output simulato: "1 file copiato."

- Metodo "echo":  
        C:\Users\User> echo Ciao mondo! > testo.txt  
        Questo comando crea o sovrascrive "testo.txt" con il testo "Ciao mondo!"  
        Per aggiungere una riga senza cancellare il contenuto esistente:  
        C:\Users\User> echo Seconda riga >> testo.txt

> Nota: Il simbolo ">" crea il file o sostituisce il contenuto esistente, mentre ">>" aggiunge il nuovo testo in coda mantenendo il contenuto già presente.

### 3.2 In Linux

**Creare una cartella:**

    user@ubuntu:~$ mkdir NuovaCartella

**Creare un file vuoto:**

    user@ubuntu:~$ touch file_vuoto.txt

**Creare un file con contenuto:**

- Metodo "echo":  
        user@ubuntu:~$ echo "Ciao mondo!" > testo.txt  
        Per aggiungere una riga senza cancellare il contenuto esistente:  
        user@ubuntu:~$ echo "Altra riga" >> testo.txt

- Metodo interattivo:  
        user@ubuntu:~$ cat > testo.txt  
        (Digitare il testo desiderato, poi premere Ctrl+D per terminare)

---

## 4. Modifica e visualizzazione del contenuto

### 4.1 In Windows

**Visualizzare il contenuto di un file:**

    C:\Users\User> type testo.txt

**Modificare il file in Notepad:**

    C:\Users\User> notepad testo.txt  
    (Viene aperto il Blocco note per modificare il file)

### 4.2 In Linux

**Visualizzare il contenuto di un file:**

    user@ubuntu:~$ cat testo.txt

**Modificare il file in Nano:**

    user@ubuntu:~$ nano testo.txt  
    (In Nano, premere Ctrl+O per salvare e Ctrl+X per uscire)

---

## 5. Cancellazione di file e cartelle

### 5.1 In Windows

**Cancellare un file:**

    C:\Users\User> del esempio.txt

**Cancellare una cartella vuota:**

    C:\Users\User> rmdir CartellaDiTest

**Cancellare una cartella e tutto il suo contenuto:**

    C:\Users\User> rmdir /s /q CartellaDiTest

### 5.2 In Linux

**Cancellare un file:**

    user@ubuntu:~$ rm esempio.txt  
    (Se necessario, usare "rm -f esempio.txt" per forzare la cancellazione)

**Cancellare una cartella e tutto il suo contenuto:**

    user@ubuntu:~$ rm -r NomeCartella

---

## 6. Esportazione dello storico della CLI

**In Windows (CMD):**

    C:\Users\User> doskey /history **>** history.txt (*crea* e sovrascrive)
    C:\Users\User> doskey /history **>>** history.txt (*crea* e aggiunge)

Questo comando salva la cronologia dei comandi eseguiti nella sessione corrente nel file "history.txt", o altro file di testo a piacere.

**In Linux:**

    user@ubuntu:~$ history > history.txt

Questo comando esporta la cronologia dei comandi (come registrata nella sessione corrente) nel file "history.txt".

---

## 7. Esercizi pratici

### Esercizio 1: Navigazione e creazione di cartelle

**Windows:**

    C:\Users\User> cd Desktop  
    C:\Users\User\Desktop> mkdir LaboratorioCLI  
    C:\Users\User\Desktop> cd LaboratorioCLI  
    C:\Users\User\Desktop\LaboratorioCLI> mkdir Progetti Test

**Linux:**

    user@ubuntu:~$ cd ~/Desktop  
    user@ubuntu:~/Desktop$ mkdir LaboratorioCLI  
    user@ubuntu:~/Desktop$ cd LaboratorioCLI  
    user@ubuntu:~/Desktop/LaboratorioCLI$ mkdir Progetti Test

### Esercizio 2: Creazione di file e scrittura

**Windows:**

    C:\Users\User\Desktop\LaboratorioCLI\Test> echo "Questo è un esempio." > notes.txt  
    C:\Users\User\Desktop\LaboratorioCLI\Test> type notes.txt

*Output atteso:*

    Questo è un esempio.

**Linux:**

    user@ubuntu:~/Desktop/LaboratorioCLI/Test$ echo "Questo è un esempio." > notes.txt  
    user@ubuntu:~/Desktop/LaboratorioCLI/Test$ cat notes.txt

*Output atteso:*

    Questo è un esempio.

### Esercizio 3: Aggiunta di contenuto

**Windows:**

    C:\Users\User\Desktop\LaboratorioCLI\Test> echo "Nuova riga aggiunta." >> notes.txt  
    C:\Users\User\Desktop\LaboratorioCLI\Test> type notes.txt

*Output atteso:*

    Questo è un esempio.  
    Nuova riga aggiunta.

**Linux:**

    user@ubuntu:~/Desktop/LaboratorioCLI/Test$ echo "Nuova riga aggiunta." >> notes.txt  
    user@ubuntu:~/Desktop/LaboratorioCLI/Test$ cat notes.txt

*Output atteso:*

    Questo è un esempio.  
    Nuova riga aggiunta.

### Esercizio 4 (facoltativo): Utilizzo di un editor testuale

**Windows:**

    C:\Users\User\Desktop\LaboratorioCLI\Test> notepad notes.txt

**Linux:**

    user@ubuntu:~/Desktop/LaboratorioCLI/Test$ nano notes.txt  
    (Modifica il file, aggiungi qualche frase, salva ed esci)

---

## 8. Mappa concettuale

```mermaid
graph LR
  A[CLI] --> B[Navigazione]
  B --> C[cd, dir / ls, ls -l]
  A --> D[Creazione File e Cartelle]
  D --> E[mkdir, touch, type nul, fsutil]
  A --> F[Modifica e Visualizzazione]
  F --> G[notepad, nano, type, cat]
  A --> H[Cancellazione]
  H --> I[del, rmdir /s /q, rm, rm -r]
```

## 9. Conclusione

Questi esempi mostrano come utilizzare la riga di comando per navigare tra le directory, creare e modificare file e cartelle, cancellare file e cartelle e persino esportare la cronologia dei comandi. I comandi sono simili in Windows e Linux, sebbene la sintassi possa variare leggermente. Con la pratica, la CLI diventerà uno strumento potente per gestire il sistema in modo rapido ed efficiente.
