import sys
import string

filename = sys.argv[1] 

words:map={}
count:int=0

for (e,li) in enumerate(open(filename,"r")):
    line = li.split()
#    print(e,line)
    for word in line:
        if not (word in words):
            words[word] = 0
        words[word] = words[word] + 1  	

print("Number of Words: ",count)
print("List of Words with counts!")
# Sortierung funktioniert nur auf Listen, nicht auf Maps.
final = sorted(words.items(),key=lambda x:-x[1])
print(final)
for i in range(len(final)):
    print(final[i][0],final[i][1])