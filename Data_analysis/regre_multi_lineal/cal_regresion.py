import regresion as rg
import os

os.system("clear")

A   =   rg.regresion("datos1.dat")
B   =   rg.regresion("datos2.dat")

A.ver()
B.ver()

