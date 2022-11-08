import mysql.connector
import pandas as pd

if __name__ == "__main__":
   
# Conexão com MySQL
    con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='hortas')
    cursor = con.cursor()

 
# Lendo o csv
    df_mysql = pd.read_csv(r"C:\Users\Cleberson\Desktop\Visual Studio\huertas-familiares-por-provincia.csv", sep=",")
       
    for i, tabela in df_mysql.iterrows():
        tabela = (tabela['provincia_id'],tabela['provincia'], tabela['2016'], tabela['2017'], tabela['2018'])
    
        query = f"INSERT INTO hortas_ano(id_provincia,provincia,ano2016,ano2017,ano2018) values {tabela}" 
        cursor.execute(query)
          
    cursor.close()
    con.commit()
    con.close()    
    

    