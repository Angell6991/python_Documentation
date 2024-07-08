import matplotlib.pyplot as plt
import numpy as np
import os

import serie_fourier as sf

os.system("clear")

x = np.linspace(-2*np.pi, 2*np.pi, 1200)
y = sf.serie(x, 10000)

#----------------Configuración_para_usar_LaTeX_en_matplotlib-------------#
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Computer Modern Roman"],})

plt.figure(facecolor="#1D1D1D")

plt.plot(x, y, color="#00CCDE", label=r"$n = 10^4$")    # color: #E53681
plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

plt.xlabel("t", color="#5AEDA3")
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], [r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"], color="#5AEDA3")
plt.xlim(-2*np.pi, 2*np.pi)

plt.ylabel("f(t)", color="#5AEDA3")
plt.yticks([-1, -0.5, 0, 0.5, 1], [r"$-1$", r"$-0.5$", r"$0$", r"$0.5$", r"$1$"], color="#5AEDA3")
plt.ylim(-1.5, 1.5)

plt.title("Serie Diente de Sierra", color="#5AEDA3", fontsize="15")

plt.gca().set_facecolor("#353535")

legend = plt.legend(fontsize=15)
legend.get_frame().set_facecolor("#1D1D1D")
legend.get_frame().set_edgecolor("#000000")
legend.get_frame().set_alpha(0.8)
legend.get_texts()[0].set_color("#5AEDA3")

# plt.savefig("grafica.png")
plt.show()
