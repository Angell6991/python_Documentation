import matplotlib.pyplot as plt
import numpy as np
import os

os.system("clear")

def f(x, n_max):
    funcion =   0
    for n in range(n_max):
        funcion =   funcion + (4/np.pi)*((np.sin(x*(1+2*n)))/(1+2*n))
    return  funcion

x_plot = np.linspace(-2*np.pi, 2*np.pi, 1000)
y_plot_5 = f(x_plot, 5) 
y_plot_50 = f(x_plot, 50) 
y_plot_inf = f(x_plot, 1000) 

leng    =   r"$  \frac{4}{\pi} \; \sum_{n=0}^{\infty} \frac{sin((2n+1)x)}{2n +1}  $"

plt.figure(facecolor="#1D1D1D")

plt.plot(x_plot, y_plot_5, color="#E53681", label=r"$ n=5 $")    
plt.plot(x_plot, y_plot_50, color="#af56fe", label=r"$ n=50$")    
plt.plot(x_plot, y_plot_inf, color="#00CCDE", label=leng)    
plt.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)

plt.xlabel("x", color="#5AEDA3")
plt.xticks(color="#5AEDA3")

plt.ylabel("f(x)", color="#5AEDA3")
plt.yticks(color="#5AEDA3")

plt.title("Funcion señal cuadrada", color="#5AEDA3", fontsize="15")

plt.gca().set_facecolor("#353535")

legend = plt.legend(fontsize=10, loc="upper right")
legend.get_frame().set_facecolor("#1D1D1D")
legend.get_frame().set_edgecolor("#000000")
legend.get_frame().set_alpha(0.8)
legend.get_texts()[0].set_color("#5AEDA3")
legend.get_texts()[1].set_color("#5AEDA3")
legend.get_texts()[2].set_color("#5AEDA3")

# plt.savefig("grafica.pdf")
plt.show()
