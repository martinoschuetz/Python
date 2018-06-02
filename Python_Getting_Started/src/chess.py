import string
i=1
n=8
str='. '*8

i=0
print(' ',end=' ')
while i < n:
    print(string.ascii_lowercase[i],"",end='')
    i=i+1

i=1
print(' ')
#print(' ','a','b','c','d','e','f','g','h')
while i <= n:

    print(i,str)
    i=i+1