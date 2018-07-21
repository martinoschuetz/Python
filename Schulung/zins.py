b = input("Betrag?")
z = input("Zins?")
l = input("Laufzeit?")

i = 0
betrag = float(b)
zins = float(z)
dauer = int(l)

while i <= dauer:
    print("Jahr %4.0f, %10.2f", (i,betrag))
#    print("Jahr ",i,"Betrag", betrag)
    betrag = betrag + betrag * zins / 100.
    i=i+1