local   lista   =   {1, 2 ,3 ,4 ,6}

print("Total de elementos en el array: "..#lista)
print("Ultimo elemento del array: "..lista[#lista])

for i = 1, #lista  do
    print("lista["..i.."] = "..lista[i])
end

print("Agregando nuevo elemnto")

lista[#lista + 1]   =   9

print("Nuevo array")

for i = 1, #lista  do
    print("lista["..i.."] = "..lista[i])
end

