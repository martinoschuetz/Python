import sys
import string
import array

filename  = sys.argv[1] 

fh = open(filename,"r")
linecount = 0

#open(filename,"r").read().count("a")

for line in fh:
    for ascii in (string.ascii_lowercase):
        for chr in line:
            if chr == ascii:
                count = count + 1



for i in in (string.ascii_lowercase):
    print("Der Buchstabe ",i,"kommt",count,"mal vor!")
