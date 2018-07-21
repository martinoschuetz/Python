import string
import sys

print(len(sys.argv))

i=0
j=1
n=8

print(' ',end=' ')
while i < n:
    print(string.ascii_lowercase[i],"",end='')
    i=i+1

i=1
print(' ')
while i <= n:
    print(i,'',end="")
    j = 1
    c ='.'
    k = 1
    while j<=n:
        c ='.'
        k=1
        while k <= len(sys.argv) - 1:
            x = int((sys.argv[k])[0])
            y = int((sys.argv[k])[1])
            l = (sys.argv[k])[2]
            if((i==x) and (j==y)):
                c=l
            k=k+1
        print(c,'',end="")
        j=j+1
    i=i+1
    print('')
