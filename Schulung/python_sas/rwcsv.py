#!/usr/bin/env python3

import sys

# ---------------------------------------------
def einlesen(filename,sep=','):
    db=[]
    fh=open(filename)
    fieldnames=fh.readline().rstrip().split(sep)
    for line in fh:
       db.append(dict(zip(fieldnames,line.rstrip().split(sep))))
    fh.close()
    return(fieldnames,db)
# ---------------------------------------------
def ausgeben(erg,outfile="",sep=','):
    (fieldnames,db)=erg
    fh=sys.stdout
    if outfile: fh=open(outfile,"w")
    print(sep.join(fieldnames),file=fh)
    for row in db:
        lst=[]
        for k in fieldnames:
            lst.append(row[k])
        print(sep.join(lst),file=fh)
    if outfile: fh.close()
# ---------------------------------------------
#def suchen( erg:Tuple[List,List[Dict]] ,k:str, v:str ) -> Tuple:
def suchen( erg ,k, v ):
    (fieldnames,db)=erg
    myerg=[]
    for row in db:
       if row[k]==v: myerg.append(row)
    return(fieldnames,myerg)

