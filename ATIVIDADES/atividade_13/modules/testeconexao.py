import pandas as pd
import psycopg2
from modules.ativ import get_dados
from modules.connector import Interface_db
import statistics as st

if __name__ == "__main__":
    try:
        interface_banco = Interface_db("postgres", "admin", "127.0.0.1", "ATIVIDADE 13")   
            
        get_dados ()
       
    except Exception as e:
        print(str(e))
