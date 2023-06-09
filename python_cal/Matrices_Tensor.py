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

x = Array([[0,0],[0,0]])
for k in range(2):
    C =Array( [ [A[0,0,k]*A[1,k,0], A[0,0,k]*A[1,k,1]], [A[0,1,k]*A[1,k,0], A[0,1,k]*A[1,k,1]] ] )
    x = x + C

print(x)
