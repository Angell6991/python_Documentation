#---| ANGELL |---#

import os
import numpy as np 

os.system("clear")

A = np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])
B = np.array([[9,8,7],
     [6,5,4],
     [3,2,1]])
C = np.array([[1,0,0],
              [0,2,0],
              [0,0,3]])

print(A)                    #Ver matriz
print(B)                    #Ver matriz 
print(A + B)                #Suma
print(A - B)                #Resta
print(np.dot(A,B))          #Producto A B
print(B[0,2])               #Ver componente 0,2 de B
print(np.linalg.det(C))     #Determinate de C
print(np.linalg.inv(C))     #Inversa de C
