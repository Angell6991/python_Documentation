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
fig = plt.figure(facecolor="#1D1D1D")
ax = fig.add_subplot(111, projection="3d")

# Graficar la superficie 3D
ax.plot_surface(X, Y, Z, color="#00CCDE")
plt.gca().set_facecolor("#353535")

# Personalizar la gráfica
ax.set_title("Titulo_gráfica", color="#5AEDA3")

ax.set_xlabel("Eje_x", color="#5AEDA3")
ax.set_ylabel("Eje_y", color="#5AEDA3")
ax.set_zlabel("Eje_z", color="#5AEDA3")

ax.xaxis.label.set_color("#5AEDA3")
ax.yaxis.label.set_color("#5AEDA3")
ax.zaxis.label.set_color("#5AEDA3")

ax.tick_params(axis='x', colors='#5AEDA3')
ax.tick_params(axis='y', colors='#5AEDA3')
ax.tick_params(axis='z', colors='#5AEDA3')

# Establecer las etiquetas de los ejes z
ax.zaxis.set_ticks([0, 0.5, 1.0])
ax.zaxis.set_ticklabels(['0', '0.5', '1.0'], color='#5AEDA3')

# Agregar ecuación como leyenda
equation_text = r'$z = \sin(\sqrt{x^2 + y^2})$'
ax.text2D(0.05, 0.95, equation_text, transform=ax.transAxes, color="#5AEDA3", fontsize=12)

# Mostrar la gráfica
# plt.savefig("grafica_3D.py")
plt.show()
