import string
import sys

print(len(sys.argv))

print(' ',end=' ')
for i in (range(1,9)):
    print(string.ascii_lowercase[i],"",end='')

i=1
print(' ')
for i in (range(1,9)):
    print(i,"",end="")
    for j in (range(1,9)):
        c ='.'
        for k in range(1,len(sys.argv)):
# annotations ab 3.6, kann man auch mit mypy checken.			
            x:int = int((sys.argv[k])[0])
            y:int = int((sys.argv[k])[1])
            l:int = (sys.argv[k])[2]
            if((i==x) and (j==y)):
                c=l
        print(c,'',end="")
    print('')
