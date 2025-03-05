################################################################
###  Programa para dividir el pago de un resibo de servicios ###
###  publicos por pisos o apartamentos de una casa           ###
################################################################
import  os

os.system("clear")

###------------------Insertando_datos----------------------###
print("Inserte datos del recibo y el numero de pisos en la casa. \n")

total_pagar_resivo  =   float(input("Total á pagar del resibo: $ "))
numero_de_pisos     =   int(input("Numero de pisos: "))

###-----------------Haciendo_calculos----------------------###
pago_por_piso       =   total_pagar_resivo/numero_de_pisos

###---------------Mostrando_resultados---------------------###
print("")
print("Datos de pago \n")
print("Valor á pagar por piso: $ " + str(round(pago_por_piso)))
print("Total á pagar del resibo: $ " + str(round(pago_por_piso*numero_de_pisos)))


