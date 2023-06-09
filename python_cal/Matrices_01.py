#---| ANGELL |---#

from sympy import*
import os

os.system("clear")

x = symbols("x")

A = Matrix([[cos(x),sin(x)],[-sin(x),cos(x)]])

B = Matrix([[cos(x),-sin(x)],[sin(x),cos(x)]])

print(A)                        #Ver matriz A 
print(diff(A,x))                #Derivar la matriz
print(A+B)                      #Suma
print(simplify(A*B))            #PRoducto de A por B
print(simplify(A.inv()))        #Inversa de A 
print(simplify(A.det()))        #Determinate de A 
print(B[0,0])                   #Ver la componete 0,0 de la matriz B
