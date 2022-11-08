from modules.conector import Interface
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