################################################################
###  Programa para dividir el pago de un resibo de servicios ###
###  publicos por persona teniendo en cuenta los pisos       ###
###  o apartamentos de una casa                              ###
################################################################
import  os

os.system("clear")

###------------------Insertando_datos----------------------###
print("Inserte datos del recibo, datos de la cantidad de personas que habitan y el numero de pisos en la casa. \n")

total_pagar_resivo  =   float(input("Total á pagar del resibo: $ "))
numero_de_pisos     =   int(input("Numero de pisos: "))

numero_de_people    =   []
for i   in  range(numero_de_pisos):
    numero_de_people.append(int(input("Numero de personas piso " + str(i+1) + ": ")))

total_people_hause  =   0
for i   in  range(numero_de_pisos):
    total_people_hause  =   total_people_hause  +   numero_de_people[i]


###-----------------Haciendo_calculos----------------------###
pago_one_people     =   total_pagar_resivo/total_people_hause

pago_piso           =   []
for i   in  range(numero_de_pisos):
      pago_piso.append(pago_one_people*numero_de_people[i])


###---------------Mostrando_resultados---------------------###
print("")
print("Datos de pago \n")

print("Valor á pagar por persona: $ " + str(round(pago_one_people)))
for i   in range(numero_de_pisos):
    print("Piso "+ str(i+1) +": $ " + str(round(pago_piso[i])))

total_pago          =   0
for i    in range(numero_de_pisos):
    total_pago  =   total_pago   +   pago_piso[i]
print("Total á pagar del resibo: $ " + str(round(total_pago)))


