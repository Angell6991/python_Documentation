import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import os

os.system("clear")

##########################################################################
##-------------------------Deniniciones_y_arreglos----------------------##
##########################################################################

#-----------------------Definiendo_funciones_á_graficar------------------#
def R_geometry(x):
    return  x

def R_physics(x):
    g   =   np.sqrt(1-(1/x))
    r_3 =   g*((x**3)+(5/4)*(x**2)+(15/8)*(x)) + (15/16)*np.log((1+g)/(1-g))
    return  np.cbrt(r_3)

#----------------------------Arreglos_á_graficar-------------------------#
x_plot_01_   =   np.linspace(1, 10, 100)
x_plot_02_   =   np.linspace(0, 10, 100)
y_plot_01_   =   R_physics(x_plot_01_)
y_plot_02_   =   R_geometry(x_plot_02_)

x_plot_01   =   np.linspace(1, 1.2, 100)
x_plot_02   =   np.linspace(1, 1.2, 100)
y_plot_01   =   R_physics(x_plot_01)
y_plot_02   =   R_geometry(x_plot_02)

#---------------------------Punto_de_intersección------------------------#

def serie(n_max):

    x   =   sp.symbols("x")
    f_0 =   x*(1-x)*((1+x)**2)
    D_list  =   [f_0.subs(x, 0).evalf()]

    for i in range(n_max):
        f_0 =   ((1-x)**3)*((1+x)**4)*sp.diff(f_0, x)
        f_val   =   f_0.subs(x, 0)
        f_val   =   f_val/((3**((i+1)+1))*(2**(i+1))*(sp.factorial((i+1)+1)))
        f_val   =   f_val.evalf()
        D_list.append(f_val)

    D_list  =   np.array(D_list)
    Delta   =   0

    for i in range(len(D_list)):
        Delta   =   Delta + D_list[i]
    
    return Delta

point   =  1 + serie(7)
nota    =  "(" + str(round(point,4)) + " , " + str(round(point,4)) + ")"

##########################################################################
##---------------------------------Plot---------------------------------##
##########################################################################

#----------------Configuración_para_usar_LaTeX_en_matplotlib-------------#
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],})

#----------------------------Configuración_plot--------------------------#
fig, axs = plt.subplots(1, 2, figsize=(12, 5), facecolor="#1D1D1D", gridspec_kw={'width_ratios': [2, 2]})

axs[0].plot(x_plot_01_, y_plot_01_, color="#00CCDE", label="R Physics")
axs[0].plot(x_plot_02_, y_plot_02_, color="#E53681", label="R Geometry")
axs[0].set_title("Intersection of Volumes", color="#5AEDA3", fontsize="15")

leng_01    =   axs[0].legend(fontsize=15, loc="upper left", facecolor="#1D1D1D", edgecolor="#000000")
leng_01.get_texts()[0].set_color("#5AEDA3")
leng_01.get_texts()[1].set_color("#5AEDA3")


axs[1].plot(x_plot_01, y_plot_01, color="#00CCDE", label="R Physics")
axs[1].plot(x_plot_02, y_plot_02, color="#E53681", label="R Geometry")
axs[1].plot(point, point, color="#ffffff", marker="o")
axs[1].set_title("Intersection of Volumes", color="#5AEDA3", fontsize="15")

leng_02    =   axs[1].legend(fontsize=15, loc="upper left", facecolor="#1D1D1D", edgecolor="#000000")
leng_02.get_texts()[0].set_color("#5AEDA3")
leng_02.get_texts()[1].set_color("#5AEDA3")

plt.annotate(nota, (point, point), textcoords="offset points", xytext=(45,-25), ha='center', color="#ffffff", fontsize="15")
plt.tight_layout(w_pad=4)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

for ax in axs.flat:
    ax.set_facecolor("#353535")
    ax.grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)
    ax.set_xlabel(r"$ \rho \; Distance \; to \; R_{e} $", color="#5AEDA3", fontsize="15")
    ax.set_ylabel(r"$ R(\rho)/R_{e} $", color="#5AEDA3", fontsize="15")
    ax.xaxis.label.set_color("#5AEDA3")
    ax.yaxis.label.set_color("#5AEDA3")
    ax.tick_params(axis='x', colors='#5AEDA3')
    ax.tick_params(axis='y', colors='#5AEDA3')

# plt.savefig("grafica.pdf")
plt.show()
