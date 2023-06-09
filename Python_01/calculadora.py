#---| @_ANGELL |---#

print("Bienbenidos  a la calculadora \nPara salir escribe exit \nLas operaciones que ouedes hacer son: \nsum, rest, mult, div ")

x = float(input("Ingrese Un numero: "))

    
while True :

    operacion   =   str(input("Ingrese operación: "))
    y           =   float(input("Ingresa el siguiente numero: "))

    if operacion.lower()    ==      "sum":
        x = x + y
        print(x)

    elif operacion.lower()    ==      "rest":
        x = x - y
        print(x)

    elif operacion.lower()    ==      "mult":
        x = x*y
        print(x)

    elif operacion.lower()    ==      "div":
        x = x / y
        print(x)

    elif operacion.lower()    ==      "exit":
        break
    
    else:
        print("operacion no valida")
        break



