import mysql.connector
import pandas as pd

# Conexão com MySQL
con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='hortas')
cursor = con.cursor()
 

# Selecionando a tabela no banco de dados
new_df = "select * from hortas_ano" 

query = cursor.execute(new_df)
query = cursor.fetchall()
new_df = pd.DataFrame(query)
print(new_df)

# Salvar o arquivo em csv
new_df.rename({0 : "id_provincia"}, axis=1, inplace=True)
new_df.rename({1 : "provincia"}, axis=1, inplace=True)
new_df.rename({2 : "ano2016"}, axis=1, inplace=True)
new_df.rename({3 : "ano2017"}, axis=1, inplace=True)
new_df.rename({4 : "ano2018"}, axis=1, inplace=True)
new_df.to_csv(f"provincia.csv", index=False)



