#---| ANGELL |---#

import sympy as sp 

x = sp.Symbol("x")      # define la variable de forma simbolica
y = x**2                # define expreción  a derivar 
ypri = sp.diff(y,x)     # deriva y respect  a x

print("Función: ", y)
print("Derivada: ", ypri)             # muestra el resultado de la derivada por terminal




