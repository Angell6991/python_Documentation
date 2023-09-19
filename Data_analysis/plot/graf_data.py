import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# funcion seno
xx = np.linspace(0, 2*np.pi, 100)
yy = np.sin(xx)
yY = np.cos(xx)

# Crear la gráfica
plt.scatter(x, y, color="red", marker="o")
plt.plot(xx ,yy)
plt.plot(xx, yY)
plt.grid(True, linestyle="dashed")

# Personalizar la gráfica 
plt.title("Nombre_Gráfica")
plt.xlabel("Nombre_eje_x")
plt.ylabel("ENombre_eje_y")

# Mostrar la gráfica
plt.show()

