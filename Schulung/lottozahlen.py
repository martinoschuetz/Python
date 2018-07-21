import random
import sys

ziehung=int(sys.argv[1])
aus=int(sys.argv[2])

ergebnisse=[]
lottozahlen=list(range(1,aus+1))
print(lottozahlen)

for i in range(ziehung):
    ergebnisse.append(lottozahlen.pop(random.randint(0,len(lottozahlen)-1)))
print(ergebnisse)