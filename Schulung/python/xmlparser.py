#!/usr/bin/python
# *- coding: utf-8 -*-
#

import re
import sys

def einlesen(filename="adrTag.txt"):

   s=open(filename).read() 

   a=re.compile("(<datensatz[^>]*>)(.*?)(<\/datensatz.*?>)",\
                   re.MULTILINE|re.DOTALL)
   b=re.compile("(<feld[^>]*>)(.*?)(<\/feld.*?>)",\
                   re.MULTILINE|re.DOTALL)
   c=re.compile("<feld([^>]*)>")
   
   e=[]
   for i in re.findall(a,s):
      d={}
      for j in re.findall(b,i[1]):
         k=re.match(c,j[0]).groups()[0]
         v=j[1]
         d[k]=v
      # oder: d=dict([ (re.match(c,j[0]).groups()[0],j[1]) for j in re.findall(b,i[1])])
      e.append(d)
   return (map( lambda x:x.strip(),e[0].keys()),e[1:])
   
def ausgeben(f,filename=""):
   (feldnamen,tabelle)=f
   out=( open(filename,"w") if filename else sys.stdout)
   print >> out, ",".join(sorted(feldnamen))
   for d in tabelle:
      print >> out, ",".join( map( lambda x:x[1], \
                      sorted(d.items(),key=lambda x:x[0]))) 

print __name__ # bei import name des moduls
   
if __name__=="__main__":
   # ------------------------------
   (feldnamen,tabelle)=einlesen("adrTag.txt")
   print feldnamen
   print tabelle
   ausgeben((feldnamen,tabelle))
   ausgeben((feldnamen,tabelle),"out.txt")

