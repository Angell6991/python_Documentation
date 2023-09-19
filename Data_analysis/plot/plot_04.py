import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)
y4 = np.sqrt(x)

# Crear la figura y los subgráficos
fig, axs = plt.subplots(2, 2, figsize=(5, 5), facecolor="#1D1D1D")

# Formato y colores similares a la gráfica del segundo código
format_params = {
    'color': "#00CCDE",
    'linestyle': '-',
    'linewidth': 2
}

# Graficar en los subgráficos con el mismo formato y colores
axs[0, 0].plot(x, y1, **format_params)
axs[0, 0].set_title('Seno', color="#5AEDA3")
axs[0, 0].legend([r"$ \sin(x) $"], 
                 fontsize=10, 
                 loc="upper right", 
                 facecolor="#1D1D1D", 
                 edgecolor="#000000"
                 ).get_texts()[0].set_color("#5AEDA3")

axs[0, 1].plot(x, y2, **format_params)
axs[0, 1].set_title('Coseno', color="#5AEDA3")
axs[0, 1].legend([r"$ \cos(x) $"], 
                 fontsize=10, 
                 loc="upper right", 
                 facecolor="#1D1D1D",
                 edgecolor="#000000"
                 ).get_texts()[0].set_color("#5AEDA3")

axs[1, 0].plot(x, y3, **format_params)
axs[1, 0].set_title('Exponencial', color="#5AEDA3")
axs[1, 0].legend([r"$ e^{-x}$ "], 
                 fontsize=10, 
                 loc="upper right", 
                 facecolor="#1D1D1D",
                 edgecolor="#000000"
                 ).get_texts()[0].set_color("#5AEDA3")

axs[1, 1].plot(x, y4, **format_params)
axs[1, 1].set_title('Raíz cuadrada', color="#5AEDA3")
axs[1, 1].legend([r"$ \sqrt{x} $"], 
                 fontsize=10, 
                 loc="upper right", 
                 facecolor="#1D1D1D",
                 edgecolor="#000000"
                 ).get_texts()[0].set_color("#5AEDA3")

# Ajustar el espaciado entre los subgráficos
plt.tight_layout()

# Personalizar el fondo de los subgráficos y colores de las etiquetas
for ax in axs.flat:
    ax.set_facecolor("#353535")
    ax.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)
    ax.set_xlabel("x", color="#5AEDA3")
    ax.set_ylabel("f(x)", color="#5AEDA3")
    ax.xaxis.label.set_color("#5AEDA3")
    ax.yaxis.label.set_color("#5AEDA3")
    ax.tick_params(axis='x', colors='#5AEDA3')
    ax.tick_params(axis='y', colors='#5AEDA3')

# Guardar la figura como archivo de imagen
# plt.savefig("grafica_tabla.png")

# Mostrar la figura
plt.show()

