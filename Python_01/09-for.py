#---| @_ANGELL |---#

for numero in range(5) : 
    print(numero)
    #break

print()

#------------------#

buscar   =  int(input("buscar numero: "))

for numero1 in range(5) :
    print(numero1)
    if numero1 == buscar :
        print("encontrado", numero1)
        break
else :
    print("numero no encontrado")

print()

#-----------------#

for char in "Ultimate Python" :
    print(char)
    
