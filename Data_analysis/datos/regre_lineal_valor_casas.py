import pandas as pd
import numpy as np
import sqlalchemy as sql
import sklearn.metrics as sk_mec
import sklearn.linear_model as sk_lineal
import os

os.system("clear")

######################################################
##----------------load_data_and_table---------------##
######################################################

#-------------inf_para_la_conexion_con_qtl-----------#
user    =   "root"
host    =   "localhost"
password    =   "password"
database    =   "datos_01"

#--------------------creando_conexion----------------#
conex   =   sql.create_engine(
        f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        )

#------------------Imporat_table---------------------#
tabla   =   pd.read_sql_table("valor_casas", con=conex)

######################################################
##--------------manipulacion_de_datos---------------##
######################################################

#-------------separando_datos_de_la_tabla------------#
x_datos =   tabla.drop(columns=["Presio"])
y_datos =   tabla["Presio"]

#------------------regresion_lineal------------------#
regre   = sk_lineal.LinearRegression()
regre.fit(x_datos, y_datos)

y_regre =   regre.predict(x_datos)

b   =   regre.intercept_
print("punto de corte: ", b)

for i in range(5):
    m   =   regre.coef_[i] 
    print(f"pendiente {i+1}: {m}")
    
print("confianza coeficiente: ", sk_mec.r2_score(y_datos, y_regre))



