import sys
import string

filename = sys.argv[1] 

fieldnames=[]
db=[]
line=[]


fh = open(filename,"r")
fieldnames = fh.readline().rstrip().split(",")

for li in fh:
    db.append(dict(zip(fieldnames, li.rstrip().split(","))))
	
fh.close()

print(db)
 
erg=[]
k="ort"
v="muenchen"
for row in db:
    if row[k]==v: erg.append(row)

print()
print(erg)

# Join als inverse operation zum split
sep=","
fh = open("d:/TMP/adr_out.csv","w")
print(sep.join(fieldnames),file=fh)
for row in db:
    lst=[]
    for k in fieldnames:
        lst.append(row[k])
    print(sep.join(lst),file=fh)
	
fh.close()