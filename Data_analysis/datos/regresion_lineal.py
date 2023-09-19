import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as sk_lineal
import sklearn.metrics as sk_mec
import os

#################################################################
##----------------------instalar_librerias---------------------##
#################################################################
##  pip pandas                                                 ##
##  pip scikit-learn                                           ##
##  pip numpy                                                  ##
##  pip matplotlib                                             ##
#################################################################

os.system("clear")

#----------importando_datos_para_la_regresion_lineal------------#
datos   =   pd.read_csv("datos_regresion.csv", delimiter=",")

datos_x =   datos["independiente_var"]
datos_x =   np.array(datos_x).reshape(-1,1)

datos_y =   datos["dependiente_var"]
datos_y =   np.array(datos_y)

#------------------------regresion_lineal-----------------------#
regre   = sk_lineal.LinearRegression()
regre.fit(datos_x, datos_y)

y_regre =   regre.predict(datos_x)
x_regre =   datos_x

b   =   regre.intercept_
m   =   regre.coef_[0] 
print("punto de corte: ", b)
print("pendiente: ", m)
print("confianza coeficiente: ", sk_mec.r2_score(datos_y, y_regre))

#-----------------------grafica_datos---------------------------#

plt.plot(x_regre, y_regre, color= "blue")

plt.scatter(datos["independiente_var"], datos["dependiente_var"], color="red", marker="o")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("grafica")

plt.grid(True, linestyle="dashed")
plt.show()

