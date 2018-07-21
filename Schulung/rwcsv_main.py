import sys
import rwcsv
#import rwcsv import *: Dann könnte man auf den Modulnamen verzichten
#import rwcsv as r

filename = "D:/TMP/adr.csv"
outfile = "D:/TMP/out.csv"
if (len(sys.argv) > 2):
    filename = sys.argv[1]
    outfile = sys.argv[1]

erg=rwcsv.einlesen(filename=filename)
(fieldnames,db)=erg
rwcsv.ausgeben(erg)
rwcsv.ausgeben(erg,outfile=outfile)
serg=rwcsv.suchen(erg,"ort","muenchen")