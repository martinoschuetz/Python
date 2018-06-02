'''
Created on 11.02.2017

@author: germsz
'''
# Methods / Functions in Python
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y+a

print(add(1,2))
print(addFixedValue(1))
print(add(3,2))
print(addFixedValue(4))

# Loops and if clauses
i = 1
for i in range(1, 10):
    if i <= 5 :
        print('Smaller or equal then 5.\n')
    else:
        print('Larger then 5.\n')

# String manipulation
s = "abcdefg"
assert (s[0:4]=="abcd")
assert (s[4:]=="efg")
assert ("abcdefg"[4:0]=="")
assert ("abcdefg"[0:2]=="ab")

#Concatenate strings and numbers
print('this is a text plus a number ' + str(10))

# Lists
mylist = ["Linux", "Mac OS" , "Windows"]
# Print the first list element
print(mylist[0])
# Print the last element
# Negativ values starts the list from the end
print(mylist[-1])
# Sublist - first and second element
print(mylist[0:2])
# Add elements to the list
mylist.append("Android")
# Print the content of the list
for element in mylist:
        print(element)
mylist = ["Linux", "Linux" , "Windows"]
# remove duplicates from the list
mylist = list(set(mylist))

#Processing files in Python
f = open('c:\\temp\\wave1_new.csv', 'r')
print(f)
for line in f:
    print(line.rstrip())
f.close()

f = open('c:\\temp\\wave1_new.csv', 'r')
output = open('c:\\temp\\sql_script.text', 'w')
for line in f:
    output.write(line.rstrip() + '\n')
f.close()

#Splitting strings and comparing lists
f1 = open('c:\\temp\\launchconfig1.txt', 'r')
s= ""
for line in f1:
    s+=line
f1.close()

f2 = open('c:\\temp\\launchconfig2.txt', 'r')
s2= ""
for line in f2:
    s2+=line
f2.close()
list1 = s.split(",")
list2 = s2.split(",");
print(len(list1))
print(len(list2))


difference = list(set(list1).difference(set(list2)))

print (difference)

#Writing Python Scripts in Unicode
# -*- coding: UTF-8 -*-

#Classes in Python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "x-value" + str(self.x) + " y-value" + str(self.y)
    def __add__(self,other):
        p = Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p

p1 = Point(3,4)
p2 = Point(2,3)
print(p1)
print (p1.y)
print (p1+p2)


