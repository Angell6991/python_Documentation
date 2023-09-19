import pandas as pd
import os
import sqlalchemy as sql

#################################################################
##---------------------instalar_librerias----------------------##
#################################################################
## pip install pandas                                          ##
## pip install mysql-connector-python                          ##
## pip install sqlalchemy                                      ##
#################################################################

os.system("clear")

#------------informaicon_para_la_conexxion_con_sql--------------# 
user = "root"
password = "contraseña"
host = "localhost"
database = "name_database_sql"

#-----------------------creando_conexion------------------------# 
conexion = sql.create_engine(
        f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        )

#----------Exportando_tabla_de_datos_mediante_la_conexion-------# 
datos = pd.read_sql_table("Nombre_table_data", con=conexion)

print(datos)
