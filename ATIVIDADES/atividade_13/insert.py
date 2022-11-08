import pandas as pd
from modules.ativ import get_dados
from modules.connector import Interface_db, get_db_info
import numpy as np
import psycopg2

# PANDAS LENDO OS ARQUIVOS CSV:
variavel_1 = pd.read_csv("DADOS_1.csv", sep=",")
variavel_2 = pd.read_csv("DADOS_1.csv", sep=",")

#EXCLUINDO ID DA PLANILHA (AXIS EXCLUI A COLUNA / INPLACE TRUE CONFIRMA ALTERAÇÃO)
variavel_1.drop(["id"], axis=1, inplace=True) 
variavel_2.drop(["id"], axis=1, inplace=True)


# EXCLUINDO AS LINHAS QUE CONTEM NULO (DROPNA = EXCLUI OS DADOS NULOS DO ARQUIVO)
new_variavel_1 = variavel_1.dropna()
new_variavel_2 = variavel_2.dropna()
# print(new_variavel_1.info())   # INFO = IMPRIMI AS INFORMAÇÕES DO DADO 
# print(variavel_1.head(40))
# print(variavel_2.head(40))


# CONCATENANDO AS 2 TABELAS 
new_variavel = pd.concat([new_variavel_1, new_variavel_2])

#(ASTYPE =  ESTA MUDANDO CAMPO DATA DE OBJECT PARA DATETIME )
new_variavel['data'] = new_variavel['data'].astype('datetime64')

#CORRIGNDO O FORMATO DA DATA
new_variavel['data'] = new_variavel['data'].dt.strftime('%d/%m/%Y')
# print(new_variavel.info())
# print(new_variavel.head(40))

try:
    interface_banco = Interface_db("postgres", "admin", "127.0.0.1", "ATIVIDADE 13")    
              
    for index, row in new_variavel.iterrows():
        interface_banco.executar(f"INSERT INTO dados(data, valor) VALUES ('{row['data']}', {int(row['valor'])})")
        
    
except Exception as e:
    print(str(e))















        
   

    