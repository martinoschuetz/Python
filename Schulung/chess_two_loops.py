import string
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
l = sys.argv[3]

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
    j=1
    c ='. '
    while j<=n:
        if((i==x) and (j==y)):
            c=l
            print(c,'',end="")
            c ='. '
        else:
            print(c,end="")
        j=j+1
    i=i+1
    print('')
