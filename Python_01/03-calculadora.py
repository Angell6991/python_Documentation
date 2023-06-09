#---| @_ANGELL |---#

n1      =   input("Ingresar primer numero: ")
n2      =   input("Ingresarsegundo numero: ")

n1      =   int(n1)
n2      =   int(n2)

print("Suma:", n1 + n2)

Suma            =   n1 + n2
resta           =   n1 - n2
multplicaion    =   n1 * n2
divicion        =   n1 / n2


print("Para los numeros", n1, "y", n2) 
print("el resultado de la suma es ", Suma)
print("el resultado de la resta es ", resta)
print("el resultado de la multiplicaion es ", multplicaion)
print("resultado de la divicion es ", divicion)


mensaje         =   f"""
Para los numeros {n1} y {n2} 
el resultado de la suma es {Suma}
el resultado de la resta es {resta}
el resultado de la multiplicaion es {multplicaion}
el resultado de la divicion es {divicion}
                    """

print(mensaje)


