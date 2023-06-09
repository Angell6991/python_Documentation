#---| ANGELL |---#

from sympy import*
import os

os.system("clear")

A = Array([
    [[1,2],[3,4]], 
    [[5,6],[7,8]], 
    [[9,10],[11,12]]
         ])

print(A)
print(A[0])
print(A[1])

DD = [[0,0],[0,0]]
x = Array([0]*4, (2,2))
for k in range(2): 
    for j in range(2):
        for i in range(2):
            DD[i][j] = A[0,i,k]*A[1,k,j]
    Dx = Array(DD)
    x = x + Dx
print(x)

