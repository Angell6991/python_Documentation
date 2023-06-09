#---| ANGELL |---#

palabra = input("Ingrese palabra: ").replace(" ","").lower()

def reverse():
    u = ""
    for char in palabra:
        u =  char + u
    return u

if reverse() == palabra :
    print("True")
else : 
    print("False")
