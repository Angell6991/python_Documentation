########################################################
###  Programa para calcular el promedio de notas     ###
###  de una lista de estudiantes                     ###
########################################################

import  pandas  as  pd
import  numpy   as  np
import  os  

os.system("clear")
os.system("ls -l")
print("")

insert_data     =   str(input("Inserte el nombre del archivo con las notas: "))
print("")

datos           =   pd.read_csv(insert_data, delimiter=";;", header=None, engine="python")
datos_read      =   datos

datos           =   datos.drop(0, axis=0)  # Elimina la primera fila (índice 0)
datos           =   datos.drop(0, axis=1)  # Elimina la primera columna (índice 0)

datos           =   np.array(datos, dtype=float) # Convierte el DataFrame en un array de NumPy de tipo float

num_filas       =   datos.shape[0]  #   numero de filas     =   cantidad de estudiantes
num_colum       =   datos.shape[1]  #   numero de columnas  =   cantidad de tareas


notas           =   ["promedio"]
for i   in  range(num_filas):
    x   =   0
    for j   in  range(num_colum):
        x   =   x   +   datos[i,j]
    x   =   x/num_colum
    notas.append(str(x))


datos_read[str(num_colum+1)]   =     notas   
print(str(datos_read) + "\n")


