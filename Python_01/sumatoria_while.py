#---| @_ANGELL |---#

#----calculo de el numero e "e de Euler" con cicli while----#

import math

f = 0
n = 0
k = int(input("Ingrese el limite superior de la sumatoria: "))

while n <= k :
    Df = 1 / math.factorial(n)
    f = f + Df
    n = n + 1

print("e ≈", f)
