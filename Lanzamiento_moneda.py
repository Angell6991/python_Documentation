import os
import math
import random

os.system('clear')

x,C,S   =   0,0,0
l       =   int(input("lanzamientos de la moneda\n"))

while ( x < l ):
    R   =   ((random.randint(0,l))%2)+1
    #print(R)  # R=1,caras y R=2,sellos #

    if R == 1:
        C   =   C + R
    else:
        S   =   S + ( R / 2 )

    x  =   x + 1

print("Frecuencia de acida")
print(C,"caras")
print(S,"sellos")
print(" ")

Pc  =   ( C / l )
pcp =   Pc*100

Ps  =   ( S / l )
psp =   Ps*100

print("Probabilidad y porcentaje")
print("caras",Pc,"---",pcp,"%")
print("sellos",Ps,"---",psp,"%")

