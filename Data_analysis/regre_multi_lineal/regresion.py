import pandas as pd
import numpy  as np

######################################################################
##---------------------lista_de_funciones---------------------------##
######################################################################
##  covar_x()           |  matriz_de_covarianza_de_x                ##
##  covar_x_inrse()     |  matriz_inversa_de_cov_de_x               ##
##  covar_yx()          |  vector_de_covarianza_de_x_and_y          ##
##  var_y()             |  varianza_de_y                            ##
##  pendiente()         |  pendientes_de_la_regrecion               ##
##  punto_corte()       |  punto_de_corte_de_la_regresion           ##
##  determinacion()     |  coeficiente_de_determinacion             ##
##  des_punto()         |  desbiacion_estandar_punto_de_corte       ##
##  des_pendiente()     |  desbiacion_estandar_punto_de_la_pendiente##
##  viw()               |  crear_texto_con_resultados               ##
##  ver()               |  print_resultados                         ##    
######################################################################
######################################################################

class regresion:

    def __init__(self,ruta_datos):
        
        #---------------------------Exportar_datos----------------------------#
        self.dat    =   pd.read_csv(ruta_datos, 
                                    delimiter = "  ", 
                                    header = None, 
                                    engine = 'python')  # Exportando datos

        #--------------------------arreglo_de_datos---------------------------#
        self.dat    =   np.array(self.dat)
        self.fil    =   self.dat.shape[0]   # Numero de filas
        self.col    =   self.dat.shape[1]   # Numero de columnas
        
        #-------separando_datos_variables_dependientes_y_independientes-------#
        self.y      =   self.dat[:,(self.col - 1)]   
        self.x      =   np.delete(self.dat, (self.col - 1), axis = 1)
        
        self.M      =  self.fil 
        self.N      =  self.col - 1 

        #------------------------promedios_de_datos---------------------------#
        self.y_pro  =   (1/self.M)*(self.y.sum())
        
        self.x_pro  =   []
        for i in range(self.N):
            self.x_pro.append((1/self.M)*(self.x[:,i].sum()))
        
        self.x_pro  =   np.array(self.x_pro)
    
    #######################################################################
    ##-----------------------------funciones-----------------------------##
    #######################################################################
    
    #-----------------------------variaciones-----------------------------#
    def Dy(self,i):
        return  self.y[i] - self.y_pro 

    def Dx(self,i,j):
        return  self.x[i,j] - self.x_pro[j]

    #-----------------------------covarianzas-----------------------------#
    def covar_x(self):
           
        def pro(i,j):
            delt  =   0
            for p in range(self.M):
                delt    =   delt    +   self.Dx(p,i)*self.Dx(p,j) 
            
            return  delt/self.M
        
        matrix  =   []
        for i in range(self.N):
            for j in range(self.N):
                matrix.append(pro(i,j))
        
        return  np.array(matrix).reshape(self.N, self.N)


    def covar_x_inrse(self):
        return  np.linalg.inv( self.covar_x() )


    def covar_yx(self):
       
        def pro(i):
            delt  =   0
            for p in range(self.M):
                delt    =   delt    +   self.Dy(p)*self.Dx(p,i) 
            
            return  delt/self.M
        
        matrix  =   []
        for i in range(self.N):
            matrix.append(pro(i))
        
        return  np.array(matrix)


    def var_y(self):
        delt  =   0
        for p in range(self.M):
            delt    =   delt    +   self.Dy(p)*self.Dy(p) 
        
        return  delt/self.M
       
    #------------------------------pendientes-----------------------------#
    def pendiente(self):
        vec     =   np.dot(self.covar_x_inrse(), self.covar_yx())
        return vec

    #----------------------------punto_de_corte---------------------------#
    def punto_corte(self):
        punto   = self.y_pro - np.dot(self.x_pro, self.pendiente())
        return  punto

    #---------------------coeficiente_de_determinacion--------------------#
    def determinacion(self):
        vec     =   np.dot(self.pendiente(), self.covar_yx()) / self.var_y() 
        return vec
    #---------------------------desviacion_estandar-----------------------#
    def des_punto(self):
        des =   (1/(self.M - self.N - 1)
                 )*self.var_y()*(1 - self.determinacion() 
                                 )*(1 + np.dot(self.x_pro, np.dot(self.covar_x_inrse(), self.x_pro)))
        des =   np.sqrt(des)
        return  des
   
    def des_pendiente(self):
        dess    =   (1/(self.M - self.N - 1)
                     )*self.var_y()*(1 - self.determinacion()
                                     )*self.covar_x_inrse() 

        des     =   []
        for i in range(self.N):
            des.append(np.sqrt(dess[i,i]))
        
        return np.array(des) 
        
    #------------------------------viw_result-----------------------------#
    def viw(self):
        porcen  =   []
        for i in range(self.N):
            porcen.append(self.des_pendiente()[i]/self.pendiente()[i])
        porcen  =   np.array(porcen)


        text    =   f"""
        Coeficiente de determinación R^2: {self.determinacion()}  
        punto de corte b: {self.punto_corte()} ± {self.des_punto()}     
        ({100*self.des_punto()/self.punto_corte()} %)  
        pendientes: {self.pendiente()} ± {self.des_pendiente()}
        ({porcen*100}%)"""
        
        return text

    def ver(self):
        print(self.viw())

