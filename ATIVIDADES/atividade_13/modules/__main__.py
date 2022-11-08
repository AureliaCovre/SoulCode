from modules.connector import Interface_db, get_db_info
import pandas as pd
import psycopg2
from modules.ativ import get_dados, calculo
from modules.connector import Interface_db
import statistics as st


if __name__ == "__main__":
    try:
        get_dados()
  
    except Exception as e:
        print(str(e))
        