import string
import sys

#print(len(sys.argv))

#[[element] * numcols] * numrows
brett=[['.'] * 9] * 9
print(brett)

# Die obere Initialisierung nimmt nur Referenzen auf Spalten, weshalb der folgende Aufruf nicht mein gewünschtes Ergebnis liefert.
brett[3][4] = 'T'
print(brett)

for i in (range(len(brett))):
    print(brett[i])