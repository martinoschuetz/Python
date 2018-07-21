import sys
import string

filename  = sys.argv[1] 

for ascii in (string.ascii_lowercase):
    count=0
    for line in open(filename,"r"):
        for chr in line:
            if chr == ascii:
                count = count + 1
    if count != 0:
	    print("Der Buchstabe ",ascii,"kommt",count,"mal vor!")
