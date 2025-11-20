import  os
import  random

###---------------limpa _pantalla------------###
os.system("clear")

###----define_la_contaseña_real_y_contador---###
password    =   "carlos"
lista_pass   =   list(password)
contador    =   1

###------el_usario_introduce_la_password-----###
input_pass  =  input("introduce la contraseña: ")

###-------metodo_de_autenticacion_pass-------###
while   input_pass  !=  password:

    if  contador == len(lista_pass):
        os.system("clear")
        print(f"la contraseña es un nombre de {len(lista_pass)} caracteres")

    pista   =   random.choice(lista_pass)
    input_pass  =   input(
            f"contraseña erronea, pista: {pista}, buelbe a intentarlo: "
    )
    contador    =   contador    +   1

os.system("clear")
print(f"contraseña correcta, intentos: {contador}")


