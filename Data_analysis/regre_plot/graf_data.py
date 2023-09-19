import matplotlib.pyplot as plt
import numpy as np
import os
import regresion as rg

os.system("clear")

# import_datos
ajuste  =   rg.regresion("datos1.dat")

# Datos
x = ajuste.x
y = ajuste.y

# print_ajuste

ajuste.ver()

# funcion de ajuste
y_ajuste = (ajuste.pendiente())*x + ajuste.punto_corte()

# Crear la gráfica
plt.scatter(x, y, color="red", marker="o", label="Datos")
plt.plot(x ,y_ajuste, color="purple", label= str(ajuste.pendiente()) + "x + " + str(ajuste.punto_corte()))
plt.grid(True, linestyle="dashed")

# Personalizar la leyenda con color de fondo
legend = plt.legend()
legend.get_frame().set_facecolor('lightgray')  # Cambiar el color de fondo

# Personalizar la gráfica 
plt.title("ajuste gráfica lineal")
plt.xlabel("eje x")
plt.ylabel("eje y")

# Mostrar la gráfica
plt.show()

