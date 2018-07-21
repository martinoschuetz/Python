
anf = int(input("Anfangsbetrag ? "))
zins = int(input("Zins ? "))
laufzeit = int(input("Laufzeit ? "))

#print(laufzeit)

faktor = 1+ (zins/100)

current=anf

for i in range(0,laufzeit):
   
   print("Jahr %3d  %10.2f" % (i, current))
   current *= faktor
