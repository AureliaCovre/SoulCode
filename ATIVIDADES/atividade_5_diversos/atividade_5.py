#Crie um código que conte por quantos segundos uma tecla é pressionada.

import time

try:
    tempo_inicial = time.time()
    tecla1 = input("Aperte uma tecla: ")

    if tecla1:
       tempo_total = time.time()
       resultado = tempo_total - tempo_inicial
       print(round(resultado,2))
   
except Exception as e:
    print(str(e))    