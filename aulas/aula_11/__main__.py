import numpy as np
from datetime import datetime as dt
from numpy.lib.function_base import median
from modules.connector import connector

#agora = dt.now()
#lista = [15, 17, 22, 23, 27, 80]
#teste = np.asarray(lista)

#media = 0
#for i in teste:
#      media = media : i
#media = media / len(teste)      
#print("media: ",(teste.mean())

#--------------------------- ----
#teste = teste.sum()
#print(teste)

#--------------------------- ----
#teste = np.median(teste)
#print(teste)
    
#--------------------------- ----
# Encontrar a média de vendas

if __name__ == "__main__":
    try:
      interface = connector("root", "aurelia1", "127.0.0.1", "mydb") 
      query = "SELECT * FROM VENDAS"
      bd_vendas = interface.buscar(query)
      
      lista_vendas = []
      media = np.median(media)
      print(media) 
      
    except Exception as e:
        print(str(e))
