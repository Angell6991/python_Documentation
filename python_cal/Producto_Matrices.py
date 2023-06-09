#---| ANGELL |---#

from sympy import*
import os

os.system("clear")

A = Array([
           [1,2,0],
           [0,1,8],
           [0,-4,1]
          ])
B = Array([
           [5,6,4],
           [7,8,5],
           [-3,1,4]
          ])

n = sqrt(len(A))

print(A)
print(B)

DD = list(range(n))
for s in range(n):
    DD[s] = list(range(n))

Produc = Array([0]*(n**2), (n,n))
for k in range(n):
    for j in range(n):
        for i in range(n):
            DD[i][j] = A[i,k]*B[k,j]
    Produc = Produc + Array(DD)
print(Produc)
