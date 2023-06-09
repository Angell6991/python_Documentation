#---| @_ANGELL |---#

#----sumatoria para calcular el numero e "e de Euler"----#

import math

f = 0
k = int(input("Ingrese el limite superior de la sumatoria: "))

for n in range(k+1) :
    Df = 1 / math.factorial(n)
    f = f + Df

print("e ≈", f)
