#---| ANGELL |---#

from sympy import*
import os

os.system("clear")

A = [
    [1,2],
    [3,4]
    ] 
B = [
    [5,6],
    [7,8]
    ]
AA =[
    [9,10],
    [11,12]
    ]
C = Array([A,B,AA])

print(C)
print(C[0,0,1])
print(Array(A) + Array(B))
print(len(C))

A1 = Array(A)
B1 = Array(B)

f = 0
for i in range(2):
    C1 = C[0,0,i]*C[1,i,0]
    f = f + C1

"""
for i in range(2):
    C1 = A1[0,i]*B1[i,0]
    f = f + C1
"""

print(f)
