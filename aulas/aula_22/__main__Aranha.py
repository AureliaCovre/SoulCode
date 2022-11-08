from modules.connector2 import Conexao
import pandas as pd
import numpy as np

if __name__ == '__main__':
    conexion = Conexao('localhost','aula_revisao','postgres','gw64709499')
    data = pd.read_csv("huertas-familiares-por-provincia.csv")
    #data.info()
    #print(data)
    data = np.array(data)
    list_postgre = []
    for item in data:
        value = tuple(item)
        #print(data)
        list_postgre.append(value)
        
    list_postgre = str(list_postgre)[1:-1]
    print (list_postgre)
    
    query = f"INSERT INTO hortas_provincia values {list_postgre};"
    conexion.manipular(query)