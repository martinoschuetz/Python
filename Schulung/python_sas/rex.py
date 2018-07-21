#!/usr/bin/python

import re
import os
import sys

a=re.compile("hu")
e=re.match(a,"abcdefg hu hu ijklm")
print "1:",e

a=re.compile("(.*)hu(.*)")
e=re.match(a,"abcdefg hu hu ijklm")
print "3:",e,e.groups()


a=re.compile("(h.*?a).*(lo)")
b=re.match(a,"hallo hallo")
print b.groups()




a="a b   c   t	e	f"
b= re.split("\s+",a)
print b


a=re.compile(".*(<.*>).*")
a=re.compile("(<[^>]+>).*")
b=re.match(a,"abc <ab cd> def <def hij>  hallo")
if b:
   print b.groups()
else:
   print "no result"


a=re.compile(".*(<[^>]+>).*")
b=re.match(a,"abc <ab cd> def <def hij>  hallo")
print b.groups()


print "------------------"
a=re.compile(".*?(<[^>]+>).*")
b=re.match(a,"abc <ab cd> def <def hij>  hallo")
print b.groups()

a=re.compile("(<)([^>]+)(>)")
c=re.findall(a,"abc <ab cd> def <def hij>  hallo")
print c


a=re.compile("<([^>]+?)>")
c=re.sub(a,"XXXXX","abc <ab cd> def <def hij>  hallo")
print c

a=re.compile("^([0-9]+)/")
for i in os.popen("nmap localhost"):
   b=re.match(a,i)
   if b!=None:
      print b.groups()

