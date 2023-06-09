#---| ANGELL |---#

lista = ["perro", "gato", "pez", "ave", "roedor"]

for x in lista:
    print(x)

# lista enumerada #
print("lista enumerada:")
for x in enumerate(lista):
    print(x)

for x in enumerate(lista):
    print(x[0])
for x in enumerate(lista):
    print(x[1])
