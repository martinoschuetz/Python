#!/usr/bin/env python3

import sys

def einlesen(filename, sep=','):
    db=[]
    fh=open(filename)
    fieldnames=fh.readline().rstrip().split(sep)

    for line in fh:
        db.append(dict(zip(fieldnames,line.rstrip().split(sep))))

    return(fieldnames,db)   

def ausgeben(erg,outfile=""):
    if outfile == "":
        fieldnames = erg[0]
        db = erg[1]
        sep=","
        print(sep.join(fieldnames))
        for row in db:
            lst=[]
            for k in fieldnames:
                lst.append(row[k])
            print(sep.join(lst))
        exit()

    fieldnames = erg[0]
    db = erg[1]
    sep=","
    fh=open("outfile","w")
    print(sep.join(fieldnames),file=fh)
    for row in db:
        lst=[]
        for k in fieldnames:
            lst.append(row[k])
        print(sep.join(lst),file=fh)
    fh.close()
	
# with open("adr.csv") as fh:
#     lkjlkjlkj
#     jkjkljklj

def suchen(erg, field, value):
    fieldnames = erg[0]
    db = erg[1]
    erg=[]

    for row in db:
        if row[field]==value: erg.append(row)
    print(erg)

    for row in erg:
       print(row['vname'],row['email'])
   



