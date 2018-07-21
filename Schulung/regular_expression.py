import re
import os
import sys

a=re.compile("hu")
e=re.match(a,"abcdefg hu hu ijklm")
print("1:", e)

a=re.compile(".*hu.*")
e=re.match(a,"abcdefg hu hu ijklm")
print("2:", e)

a=re.compile("(.*)hu(.*)")
e=re.match(a,"abcdefg hu hu ijklm")
print("3:", e, e.groups)