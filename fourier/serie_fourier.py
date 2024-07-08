import numpy as np

###--------def_funtion-------###
def serie(time, k):
    j   =   0
    for i in range(k):
        j   =   j   +   (((-1)**((i+1)+1))/(i+1))*np.sin((i+1)*time)

    return (2/np.pi)*j

