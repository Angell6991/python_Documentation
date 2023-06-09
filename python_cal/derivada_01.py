#---| ANGELL |---#

import sympy as sp 
import os

os.system("clear")

x = str(input("Ingrese variable independiente: "))
var1 = sp.Symbol(x)      

var2 = input("Ingrese la función, a derivar: ")
orden = int(input("Orden de la derivada: "))
Derivada = sp.diff(var2, var1, orden)   # simplify()   factor()

print("Derivada:", Derivada)             

# -- Evaluando la derivada -- #

evall = str(input("¿Desea evaluar la derivada?: ")).lower().replace(" ", "")

if evall == "si" :
    valor = int(input(f"Ingrese el valor {x} = "))
    evallderivada = Derivada.subs(var1, valor)
    print("Derivada evaluada:", evallderivada)

else :
    print("exit")
