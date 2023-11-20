import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

os.system("clear")

# Datos de ejemplo
x = np.linspace(-1, 1, 3000)
y = np.linspace(-1, 1, 3000)
X, Y = np.meshgrid(x, y)
Z_1 = np.sqrt(1 - X**2 - Y**2)

t = np.linspace(0, 15*np.pi,1000)
xx = np.cos(t)*np.sin(t/30)
yy = np.sin(t)*np.sin(t/30)
zz = np.cos(t/30)

# Crear la figura y los ejes 3D
fig = plt.figure(facecolor="#1D1D1D")
ax = fig.add_subplot(111, projection="3d")

# Graficar la superficie 3D
ax.plot_surface(X, Y, Z_1, color="#1D1D1D", alpha= 0.2)
ax.plot(xx, yy, zz, color="#00CCDE")
plt.gca().set_facecolor("#353535")

# Personalizar la gráfica
ax.set_title("Trayectoria", color="#5AEDA3")

ax.set_xlabel("Eje_x", color="#5AEDA3")
ax.set_ylabel("Eje_y", color="#5AEDA3")
ax.set_zlabel("Eje_z", color="#5AEDA3")

ax.xaxis.label.set_color("#5AEDA3")
ax.yaxis.label.set_color("#5AEDA3")
ax.zaxis.label.set_color("#5AEDA3")

ax.tick_params(axis='x', colors='#5AEDA3')
ax.tick_params(axis='y', colors='#5AEDA3')
ax.tick_params(axis='z', colors='#5AEDA3')

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([0,1])

# Agregar ecuación como leyenda
equation_text = r'Surface'
ax.text2D(0.05, 0.95, equation_text, transform=ax.transAxes, color="#5AEDA3", fontsize=12)

# Mostrar la gráfica
# plt.savefig("grafica_3D.pdf")
plt.show()
