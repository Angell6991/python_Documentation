import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as sk_lineal
import sklearn.preprocessing as sk_pre
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

#--------transformando_caracteristicas_en_carc_polinomicas------#
x_poli  =   sk_pre.PolynomialFeatures(degree=2)
x_poli  =   x_poli.fit_transform(datos_x)

#-----------------regresion_lineal_multilineal------------------#
regre   = sk_lineal.LinearRegression()
regre.fit(x_poli, datos_y)

y_regre =   regre.predict(x_poli)
x_regre =   datos_x

a_0   =   regre.intercept_
a_1   =   regre.coef_[0] 
a_2   =   regre.coef_[1]
print("coeficiente de grado 0: ", a_0)
print("coeficiente de grado 1: ", a_1)
print("coeficiente de grafo 2: ", a_2)
print("confianza coeficiente: ", sk_mec.r2_score(datos_y, y_regre))

#-----------------------grafica_datos---------------------------#

plt.plot(x_regre, y_regre, color= "blue")

plt.scatter(datos["independiente_var"], datos["dependiente_var"], color="red", marker="o")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("grafica")

plt.grid(True, linestyle="dashed")
plt.show()

