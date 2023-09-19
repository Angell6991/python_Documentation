import pandas as pd
import numpy as np
import sqlalchemy as sql
import sklearn.metrics as sk_mec
import sklearn.model_selection as sk_selec
import sklearn.preprocessing as sk_pre
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
tabla   =   pd.read_sql_table("admision_data", con=conex)

######################################################
##--------------manipulacion_de_datos---------------##
######################################################

#-------------separando_datos_de_la_tabla------------#
x_datos =   tabla.drop(columns=["Admitido"])
y_datos =   tabla["Admitido"]

# print(tabla.iloc[0]) #visualizar una fila de la tabla 

#-------------datos_entremamiento_y_prueva-----------#
x_train, x_test, y_train, y_test    =   sk_selec.train_test_split( 
        x_datos, y_datos, test_size=0.2)

#---------------regresion_lineal_and_logi------------#
regre   =   sk_lineal.LogisticRegression()
regre.fit(x_train, y_train)

y_regre =   regre.predict(x_test)

presicion_model =  sk_mec.accuracy_score(y_test, y_regre) 
print("Presición del modelo: ", presicion_model, "\n")

print("admitidos_text:", np.array(y_test), "\n")
print("admitidos_predic:", y_regre, "\n")

