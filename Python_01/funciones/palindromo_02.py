#---| ANGELL |---#

texto = input("Ingrese palabra: ").replace(" ","").lower()

def reverse(palabra):
    palabra = texto
    u = ""
    for char in palabra:
        u = char + u
    return u

if reverse(texto) == texto:
    print("True")
else:
    print("False")
