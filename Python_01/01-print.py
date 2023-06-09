#---|| @_ANGELL ||---#

"""Comentario"""

# print() Muestra por pantalla el contenido entre parentesis
print("Hola mundo!")

# salto de linea: \n
print("Hola \n Mundo!")

# mostar comillas : \"
print("Hola \"Mundo!\" \n")

# el * numero, luego del contenido de comillas hace que ese contenido se repita ese nuemro de veces  
print("Un comentario repetido " * 4 ,"\n")


"""Forma de definir Variables"""

nombre_01   = "Ultimate Python"
nombre_02   = """Este texto es un texto largoo, que sirve para probar la longitud de textos"""
x           = 12    # numero entero
y           = 13.2  # nuemro flotante


# Muestra por pantalla las Variables especificadas
print(nombre_01, x, y, "\n")

# nuestra por pantalla la variable : nombre_02
print(nombre_02, "\n")

# len() : esta funcion mide la longitud o muestra la cantidad de caracteres de la variable
print("longitud del texto anterior ", len(nombre_02), "\n")

# el parentesis cuadrado [] despues de la variable sirve para buscar un caracter, en este caso [0] busca la "componete" numero cero de la caviable  
print(nombre_01[0], "\n")

# [0:9] escoge desde el caracter cero hasta el noveno y muetra por pantalla
print(nombre_01[0:9], "\n")

# .upper es una clase, y esta al final de la vairable hace que la variable se muestre en mayusculas
print(nombre_01.upper(), "\n")

# .find: busca el caracter Py  deltro de la variable y dice su pocicion
print(nombre_01.find("Py"), "\n")

# .replace(): remplaza el caracter Ul por Py
print(nombre_01.replace("Ul","Py") ,"\n")

# Busca Ul dentro de la variable y dice sí es cirto que esta 
print("Ul" in nombre_01, "\n")

# Busca el caracter Ul dentro de la variable y dice sí es cirto que no esta
print("Ul" not in nombre_01)

