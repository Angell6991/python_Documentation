import matplotlib.pyplot as plt
import numpy as np
import os 

os.system("clear")

# Datos_de_ejemplo
theta   =   np.linspace(0, 2*np.pi, 100)
r       =   2*theta

# crear_graf_polar
plt.polar(theta, r, color="red")
plt.grid(True, linestyle="dashed")

# opcciones_graf
plt.title("titulo_graf")
plt.xlabel("angulo")
ajuste  =   plt.ylabel("radio")
ajuste.set_position((-0.1, 0.6))  # Ajustar la posición de la etiqueta eje y

# Graficar
plt.show()

