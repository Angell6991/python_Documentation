import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

os.system("clear")

# Datos de ejemplo
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Graficar la superficie 3D
ax.plot_surface(X, Y, Z, color="red")

# Personalizar la gráfica
ax.set_title("Titulo_gráfica")
ax.set_xlabel("Eje_x")
ax.set_ylabel("Eje_y")
ax.set_zlabel("Eje_z")

# Mostrar la gráfica
plt.show()
