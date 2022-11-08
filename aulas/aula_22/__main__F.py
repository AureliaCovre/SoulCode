import mysql.connector
import pandas as pd

# Método direto
if __name__ == '__main__':
    
    #informações de conexão com o banco
    con = mysql.connector.connect(user='root', password='aurelia', host='127.0.0.1', database='hortas')
    cursor = con.cursor()
        
    # ler o csv
    df = pd.read_csv(r"huertas-familiares-por-provincia.csv", sep = ",")
    
    for I, tabela in df.iterrows():
        tabela = (tabela["provincia_id"],tabela["provincia"],tabela["2016"],tabela["2017"],tabela["2018"])
        query = f"INSERT INTO hortas_ano(id_provincia,provincia,ano2016,ano2017,ano2018) values {tabela}" 
        cursor.execute(query)
    cursor.close()
    con.commit()
    con.close()