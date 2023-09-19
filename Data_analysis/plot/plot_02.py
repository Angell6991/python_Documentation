import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

theta = np.linspace(0, 2*np.pi, 100)
r = 2*theta

plt.figure(facecolor="#1D1D1D")

plt.polar(theta, r, color="#00CCDE", label=r"$ 2 \theta $")    # color: #E53681
plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

plt.xlabel(r"$\theta$", color="#5AEDA3")
plt.xticks(color="#5AEDA3")

plt.ylabel(r"$r(\theta)$", color="#5AEDA3").set_position((-0.1, 0.6))
plt.yticks(color="#5AEDA3")

plt.title("Polar plot", color="#5AEDA3", fontsize="15")

plt.gca().set_facecolor("#353535")

legend = plt.legend(fontsize=18)
legend.get_frame().set_facecolor("#1D1D1D")
legend.get_frame().set_edgecolor("#000000")
legend.get_frame().set_alpha(1.0)
legend.get_texts()[0].set_color("#5AEDA3")

# plt.savefig("grafica_polar.png")
plt.show()
