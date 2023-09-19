from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system("clear")

tabla_datos =   pd.read_csv("tabla1.csv", delimiter=",")

print(tabla_datos)

#------------------------grafica_de_puntos--------------------------#
#graf_point  =   tabla_datos.plot.scatter("variablex","variabley",
#                                         color="red",
#                                         marker="o")

#graf_point.set_xlabel("eje x")
#graf_point.set_ylabel("eje y")

#plt.grid(True, linestyle="dashed")
#plt.show()


#------------------------grafica_de_puntos--------------------------#
graf_hex  =   tabla_datos.plot.hexbin("variablex","variabley",
                                        sharex=False,
                                        gridsize=30,
                                        cmap="Reds")  # "cool" "binary"  "Greens" "Reds"

graf_hex.set_xlabel("eje x")
graf_hex.set_ylabel("eje y")

plt.grid(True, linestyle="dashed")
plt.show()




