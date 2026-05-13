io.write("Cual es tu nombre: ")
local   name    =   io.read()

io.write("¿Que año nacistes? ")
local   year    =   tonumber(io.read())

io.write("¿Que año es? ")
local   current_year    =   tonumber(io.read())

print("\n Hola "..name.. ", tu edad es: "..current_year - year)
