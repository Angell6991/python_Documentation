import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as sk_lineal
import sklearn.preprocessing as sk_pre
import sklearn.metrics as sk_mec
import sklearn.model_selection as sk_selec
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

#-------------------creando_lista_de_datos----------------------#
num_variables   =   1
num_datos       =   10

datos_x = np.random.randn(num_datos, num_variables)
datos_y = np.random.randint(2, size=num_datos)

# datos_x =   np.array(datos_x).reshape(-1,1)
# datos_y =   np.array(datos_y)

#---dibidiendo_los_datos_en_conjunto_de_entrenamiento_y_prueva--#
x_train, x_test, y_train, y_test = sk_selec.train_test_split(
        datos_x, datos_y, test_size=0.2)

#------------------regresion_lineal_logistica-------------------#
regre   = sk_lineal.LogisticRegression()
regre.fit(x_train, y_train)

y_regre =   regre.predict(x_test)  #prediccion
x_regre =   x_test

print("precisión del modelo: ", sk_mec.accuracy_score(y_test, y_regre))

#-----------------------grafica_datos---------------------------#

plt.plot(x_regre, y_regre, color= "purple")

plt.scatter(x_train, y_train, color="red", marker="o")
plt.scatter(x_test, y_test, color="blue", marker="x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("grafica")

plt.grid(True, linestyle="dashed")
plt.show()

