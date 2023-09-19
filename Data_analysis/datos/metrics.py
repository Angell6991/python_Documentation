from matplotlib import legend
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system("clear")

table_data  =   pd.read_csv("tabla.csv")

#----------------------tabla-de_datos--------------------------#
print("Table data: \n", table_data, "\n")

#----mediana_ó_valor_que_esta_en_medio_de_la_lista_de_datos----#
print("median: ", table_data["edad"].median())

#-----------------media_ó_promedio_de_datos--------------------#
print("mean: ", table_data["edad"].mean())

#-------------------desviacion_estandar------------------------#
print("standard deviation: ", table_data["edad"].std())

#---------------probabilidad_de_error_relativo-----------------#
print("probability deviation: ", table_data["edad"].std()/table_data["edad"].mean())

#-------------------porcentaje_de_error------------------------#
print("error: ", (table_data["edad"].std()/table_data["edad"].mean())*100, "%")


#-----------diagrama_de_bloques_ó_caja_y_bigotes---------------#
#graf_blok    =   table_data["edad"].plot.box(color="red")
#graf_blok.set_ylabel("años")

#plt.grid(True, linestyle="dashed")
#plt.show()

#--------------------------histograma--------------------------#
#graf_his    =   table_data["edad"].plot.hist(
#        color="red", 
#        bins=10, 
#        alpha=0.5, 
#        edgecolor="black", 
#        linestyle="solid")

#graf_his.set_ylabel("frecuencia")
#graf_his.set_xlabel("años")

#plt.show()

#----------------------digrama_de_barras-----------------------#
#graf_bar    =   table_data.plot.bar("nombre", "edad", 
#                        color="red",
#                        alpha=0.5,
#                        legend=False,
#                        edgecolor="black",
#                        linestyle="solid") 

#graf_bar.set_ylabel("Años")
#graf_bar.set_xlabel("Nombres")

#plt.show()



