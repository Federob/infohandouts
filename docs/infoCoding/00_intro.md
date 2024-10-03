# Rappresentazione delle Informazioni

In questo capitolo vedremo come funziona sommariamente il sistema di numerazione binario e lo utilizzeremo per cercare di rappresentare alcune delle informazioni
di base più importanti!


<!--  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->
## Il sistema binario



Il sistema di numerazione binario è un sistema numerico ***posizionale*** e ***in base 2***, cioè che utilizza solo 2 cifre, solitamente 0 e 1, 
per la rappresentazione di tutti i numeri.

Un sistema di numerazione posizionale è quello che da valore alle cifre di un numero a seconda della posizione che queste vi occupano.

Ad esempio nel numero decimale 37 tutti sappiamo benissimo che nonostante la cifra 3 sia più piccola della cifra 7, questa valga di più perché occupa la posizione delle decine, 
mentre la cifra più grande vale meno perché occupa la posizione delle unità

```
37   =   3 x 10   +   7 x 1
```

Questo modo di ragionare e di scrivere i numeri deriva dal fatto che siamo abituati a lavorare in base 10, poiché abbiamo 10 dita e fin da bambini il 10 era sempre il punto d'arrivo della conta sulla dita.

Nonostante ciò, altri modi di contare si sono sviluppati nella storia. Ad esempio le uova si contano a dozzine (per questo si vendono solitamente a gruppi di 6: due gruppi = una dozzina), i minuti e i secondi si contano a gruppi di sessanta, le ore a gruppi di 24 e così via.

Nell'aritmetica decimale esistono 10 cifre diverse (da 0 a 9) e quando si deve indicare un numero più grande di 9, si comincia a raggruppare mettendo in evidenza “a gruppi di 10”. 
Ecco che

```
37   =   3 decine   +   7 unità
```

Allo stesso modo si continua con le centinaia, che sono formate da 10 decine e così via. Ad esempio:

```
582   =       500       +      80      +       2

      =   5 centinaia   +   8 decine   +   2 unità

      =     5 x 100     +    8 x 10    +     2x1

      =     5 x 10 alla 2    +   8 x 10 alla 1   +   2 x 10 alla 0
```

Notiamo soprattutto l'ultima rappresentazione. In questo modo si può indicare ogni gruppo con un indice dato dalla potenza da assegnare alla base per ottenerne il peso. Infatti le unità sono il gruppo 0 (10<sup>0</sup> = 1), le decine sono il gruppo 1 (10<sup>1</sup> = 10), le centinaia il gruppo 2 (10<sup>2</sup> = 100) e così via praticamente all'infinito.

Se lavoriamo in base 2 con solo 2 cifre, gli unici numeri facili da rappresentare saranno proprio 0 e 1, mentre per 2 dovremo già iniziare a raggruppare. Così ad esempio:

```
3 = 1 coppia  + 1 unità

5 = 1 doppia coppia + 0 coppie + 1 unità
```

Vediamo i primi 10 numeri rappresentati nel sistema di numerazione binaria:

<br>

|**Decimale**|**Binario**|
|         -: |        -: |
|0|0|
|1|1|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|
|7|111|
|8|1000|
|9|1001|

<br>

Seguendo l'esempio precedente potremo stabilire una rappresentazione dei valori indicati in un numero binario:


> 1001  =<br>
> <br>
> =  1 x 2<sup>3</sup>  +  0 x 2<sup>2</sup>  +  0 x 2<sup>1</sup>  +  1 x 2<sup>0</sup>  = <br>
> <br>
> =   1 x 8   +   0 x 4   +   0 x 2   +   1 x 1   = <br>
> <br>
> =     8     +     0     +     0     +     1     =   9


In questo modo dato un qualsiasi numero binario (una sequenza di zeri e uni), potremo stabilire quale quantità esso rappresenti in decimale semplicemente applicando la metodologia appresa.

Quale valore rappresenta il numero binario `101011`?


> 101011 =<br>
> <br>
> =  1 x 2<sup>5</sup>  +  0 x 2<sup>4</sup>  +  1 x 2<sup>3</sup>  +  0 x 2<sup>2</sup>  +  1 x 2<sup>1</sup>  +  1 x 2<sup>0</sup>  = <br>
> <br>
> =   1 x 32  +   0 x 16  +   1 x 8   +   0 x 4   +   1 x 2   +  1 x 1  = <br>
> <br>
> =    32    +    0     +    8    +    0    +    2     +    1    = <br>
> <br>
> =   43



Al contrario se vogliamo capire qual è la rappresentazione binaria di un numero decimale dobbiamo utilizzare la tecnica delle divisioni (intere) successive.

Ad esempio, dato il numero 35, la sua rappresentazione binaria si ottiene dividendo (con resto) successivamente il numero fino ad ottenere quoziente zero; 
alla fine si prende la fila dei resti ottenendo una sequenza di zeri e uni che sono il numero binario.

```
35 / 2 = 17 con resto di 1

17 / 2 =  8 con resto di 1

 8 / 2 =  4 con resto di 0
 
 4 / 2 =  2 con resto di 0
 
 2 / 2 =  1 con resto di 0
 
 1 / 2 =  0 con resto di 1
```
 
da cui si desume che 

```
35 (in base 10) = 100011 (in base 2)
```



### Esercizi


**Esercizio 301**

Convertire in binario i seguenti numeri decimali:

```
23, 65, 109, 15, 48, 77, 12
```

<hr>

**Esercizio 302**

Convertire in decimale i seguenti numeri binari:

```
10, 100, 1100, 10101010, 11001100, 11110000, 10010010, 10010110
```

[Esercitati e gioca online!!](https://learningcontent.cisco.com/games/binary/index.html)


