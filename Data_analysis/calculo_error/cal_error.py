import numpy as np
import pandas as pd

######################################################################
##---------------------lista_de_funciones---------------------------##
######################################################################
##   promedio()             |   prdedio de los datos                ##
##   cuadratica_media()     |   incertudumbre cudratica media       ##
##   Er()                   |   incertidumbre relativa              ##
##   Ep()                   |   incertidumbre porsentual            ##
##   ver()                  |   hacer un print de los calculos      ##
######################################################################
######################################################################

class error:
    
    def __init__(self, ruta_datos):

        self.dat    =   pd.read_table(ruta_datos)   # Ruta de los datos á exportar
        self.dat    =   np.array(self.dat)
        self.n      =   len(self.dat)
        self.A      =   []

        for i in range(self.n):
            self.A.append(self.dat[i][0])

        self.A      =   np.array(self.A)            # Datos de forma matricial

        #-------------------------Promedio_de_datos---------------------------#
        self.pro    =   0
        for i in range(self.n):
            self.pro    =   self.pro + self.A[i]

        self.pro =   self.pro / self.n

        #---------------------------Raiz_de_la_variaza------------------------#
        self.var    =   0
        for i in range(self.n):
            self.var    =   self.var + (np.abs(self.A[i] - self.pro))**2

        self.Dd     =   np.sqrt( self.var / (self.n))

        #--------------------Certidumbre_de_desviacion------------------------#
        self.E_r    =   self.Dd / self.pro

        #-------------------Porcentaje_de_incertidumbre-----------------------#
        self.E_p    =   self.E_r*100

        #---------------------------view_result-------------------------------#
        self.view   =   f"""
        Promedio y desviación: {self.pro} ± {self.Dd}
        Certidumbre de desviacion: {self.E_r}
        Porcentaje de incertidumbre: {self.E_p} % """

    #-----------------------------funciones-------------------------------#

    def promedio(self):
        return self.pro

    def cuadratica_media(self):
        return self.Dd

    def Er(self):
        return self.E_r

    def Ep(self):
        return self.E_p

    def ver(self):
        return print(self.view)

