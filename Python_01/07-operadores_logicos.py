#---| @_ANGELL |---#

# and : y
# or  : ó
# not : negación

x   =   int(input("ingrese edad persona 1 \n"))
y   =   int(input("ingrese edad persona 2 \n"))

if x > 18 and y > 18 :
    print("las personas 1 y 2 son mayores de edad")

elif x > 18 or y > 18 :
    print("Solo una de las dos personas es mayor de  edad")

else :
    print("ambos son menores de edad")
