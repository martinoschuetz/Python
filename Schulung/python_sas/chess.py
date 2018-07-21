#!/usr/bin/env python3

import sys

# ------------------------------------------------
chess=[]
for _ in range(9): 
    row=[]
    for _ in range(9): row.append('.')
    chess.append(row)
# ------------------------------------------------
for p in sys.argv[1:]:
    chess[int(p[0])][int(p[1])]=p[2]
# ------------------------------------------------
print()
print("  a b c d e f g h")
for y in range(1,9):
    print(y,end="")
    for x in range(1,9):
       print("",chess[x][y],end="")
    print()
print()








