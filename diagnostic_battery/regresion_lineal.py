import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as sk_mec
import sklearn.linear_model as sk_lineal

os.system("clear")

ruta    =   ["battery_charge/", "battery_discharge/"]
name    =   ["Battery charge", "Battery discharge"]

for i   in  range(len(ruta)):

    #------------------Imporat_table---------------------#
    tabla   =  pd.read_csv(str(ruta[i])+"data.dat", delimiter=";;", header = None, engine = 'python') 

    ######################################################
    ##--------------manipulacion_de_datos---------------##
    ######################################################

    #-------------separando_datos_de_la_tabla------------#
    x_datos00 =   np.array(tabla[0]).reshape(-1,1)
    y_datos00 =   np.array(tabla[1]).reshape(-1,1)


    #-------combersion_de_data_segundos_a_ minutos-------#
    x_minutos   =   []
    for j   in  range(len(x_datos00)):
        x_minutos.append(x_datos00[j]/60)
    
    x_datos =   np.array(x_minutos)
    y_datos =   y_datos00


    #------------------regresion_lineal------------------#
    regre   = sk_lineal.LinearRegression()
    regre.fit(x_datos, y_datos)

    print("Data "+str(name[i]))

    y_regre =   regre.predict(x_datos)

    b   =   regre.intercept_
    print("punto de corte: ", b)

    for k   in  range(1):
        m   =   regre.coef_[k] 
        print(f"pendiente {k+1}: {m}")
        
    print("confianza coeficiente: ", sk_mec.r2_score(y_datos, y_regre))
    print(" ")

    ######################################################
    ##----------------graficando_datos------------------##
    ######################################################

    #-----------------datos_á_graficar-------------------#
    x_graf00 = np.array(tabla[0])
    x_min_graf = []
    for p   in  range(len(x_graf00)):
        x_min_graf.append(x_graf00[p]/60)


    x_graf = np.array(x_min_graf)
    y_graf = np.array(tabla[1])

    x_graf_reg  =   x_datos
    y_graf_reg  =   y_regre

    #---------creando_y_modificando_la_grafica-----------#
    plt.figure(facecolor="#1D1D1D")

    plt.plot(x_graf_reg, y_graf_reg, color="#00CCDE", label= r"$f(t) = $" + str(m) + r"$t + $" + str(b), zorder=1)    
    plt.scatter(x_graf, y_graf, color="#E53681", marker="o",zorder =2)
    plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

    plt.xlabel("Tiempo (minutos)", color="#5AEDA3")
    plt.xticks(color="#5AEDA3")

    plt.ylabel("Porcentaje de bateria (%)", color="#5AEDA3")
    plt.yticks(color="#5AEDA3")

    plt.title(str(name[i]), color="#5AEDA3", fontsize="15")

    plt.gca().set_facecolor("#353535")

    legend = plt.legend(fontsize=10)
    legend.get_frame().set_facecolor("#1D1D1D")
    legend.get_frame().set_edgecolor("#000000")
    legend.get_frame().set_alpha(0.8)
    legend.get_texts()[0].set_color("#5AEDA3")

    plt.savefig(str(ruta[i])+"grafica.pdf")
    plt.savefig(str(ruta[i])+"grafica.png")

