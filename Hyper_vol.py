import matplotlib.pyplot as plt
import scipy.special as sc 
import numpy as np
import os

os.system("clear")

x = np.linspace(-5, 30, 100)
y_1 = (np.pi**(x/2))/sc.gamma(1 + x/2) 
y_2 = x*(np.pi**(x/2))/sc.gamma(1 + x/2) 

#----------------Configuración_para_usar_LaTeX_en_matplotlib-------------#
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],})

plt.figure(facecolor="#1D1D1D")

plt.plot(x, 
         y_1, 
         color="#00CCDE", 
         label=r"$\frac{\pi^{\frac{x}{2}}}{\Gamma \left( 1 + \frac{x}{2} \right) }$")    # color: #E53681
plt.plot(x, y_2, 
         color="#E53681", 
         label=r"$\frac{x \; \pi^{\frac{x}{2}}}{\Gamma \left( 1 + \frac{x}{2}\right)}$")    # color: #E53681
plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

plt.xlabel("x", color="#5AEDA3")
plt.xticks(color="#5AEDA3")
plt.xlim(1, 25)

plt.ylabel("f(x)", color="#5AEDA3")
plt.yticks(color="#5AEDA3")

plt.title("Hyper vol and surface", color="#5AEDA3", fontsize="15")

plt.gca().set_facecolor("#353535")

legend = plt.legend(fontsize=20)
legend.get_frame().set_facecolor("#1D1D1D")
legend.get_frame().set_edgecolor("#000000")
legend.get_frame().set_alpha(0.8)
legend.get_texts()[0].set_color("#5AEDA3")
legend.get_texts()[1].set_color("#5AEDA3")

# plt.savefig("grafica.png")
plt.show()
