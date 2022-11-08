""" CREATE KEYSPACE IF NOT EXISTS hortas WITH replication = {'class' : 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS hortas_ano (
provincia_id int primary key,
provincia text,
ano2016 int,
ano2017 int,
ano2018 int
);
"""

from modules.connector import Interface
import pandas as pd

if __name__ == "__main__":
    
    # Leitura do arquivo csv:
    df_horta = pd.read_csv("huertas-familiares-por-provincia.csv")
    
    
    ##################################
    # Inserção dos dados no Cassandra:
    ##################################
    
    # Cria uma instância:
    interface_db_cassandra = Interface("hortas")
    
    # Testa conexão com o Cassandra:
    interface_db_cassandra.connection_cassandra()
    
      
    
    ##############################
    # Inserção dos dados no MySQL:
    ##############################
    
    # Cria uma instância:
    interface_db_mysql = Interface("hortas")

    # Testa conexão com o MySQL:
    interface_db_mysql.connection_mysql()
