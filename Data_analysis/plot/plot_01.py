import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.figure(facecolor="#1D1D1D")

plt.plot(x, y, color="#00CCDE", label=r"$ \frac{1}{1 + e^{-x}}$")    # color: #E53681
plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

plt.xlabel("x", color="#5AEDA3")
plt.xticks(color="#5AEDA3")

plt.ylabel("f(x)", color="#5AEDA3")
plt.yticks(color="#5AEDA3")

plt.title("Funcion sigmoide", color="#5AEDA3", fontsize="15")

plt.gca().set_facecolor("#353535")

legend = plt.legend(fontsize=20)
legend.get_frame().set_facecolor("#1D1D1D")
legend.get_frame().set_edgecolor("#000000")
legend.get_frame().set_alpha(1.0)
legend.get_texts()[0].set_color("#5AEDA3")

# plt.savefig("grafica.png")
plt.show()
