import random
import sys

mehrfach=int(sys.argv[1])
ziehung=int(sys.argv[2])
aus=int(sys.argv[3])
print(mehrfach,ziehung,aus)

alle=[]
ergebnisse=[]
lottozahlen=list(range(1,aus+1))
print(lottozahlen)

for i in range(mehrfach):
    ergebnisse=[]
    lottozahlen=list(range(1,aus+1))
    for j in range(ziehung):
        ergebnisse.append(lottozahlen.pop(random.randint(0,len(lottozahlen)-1)))
    alle.append(ergebnisse)	

for i in (range(len(alle))):
    print(alle[i])

# Verteilungen zahlen
verteilung=[]
local=[]
for i in (range(mehrfach)):
    local=[]
    for j in (range(aus)):
        count = alle[i].count(j+1)
        local.append(count)  
    verteilung.append(local)

final=[]
for i in (range(len(verteilung))):
    print(verteilung[i])
    final = final + verteilung[i]
print(final)