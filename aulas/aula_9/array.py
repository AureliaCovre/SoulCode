from logging import exception
from time import time
import numpy as np

# DESSE JEITO AJUSTAMOS O NUMERO DE LINHAS EM COLUNAS NO RESHAPE
#array = np.arange(100).reshape(10,10)
#print(array)

# ASSIM ELE RODA O COD EM SEQUENCIA
#array = np.arange(100)
#print(array)

#AQUI ELE DEMORA PQ VAI LISTANDO CADA NUMERO
#array_x = np.arange(1000)
#array_y = np.arange(1000)
#for i in array_x:
#    for j in array_y:
#       print(i+j)
        
#PRA CALCULAR O TEMPO DE PROCESSAMENTO DE DADOS
import time
inicial = 0
try:
    array_x = np.arange(1000)
    array_y = np.arange(1000)
    for i in array_x:
        for j in array_y:
           print(i+j) 
    final =time.time()
    tempo_final = final - inicial        
    print(tempo_final)        
                 
except exception as e:
    print(str(e))         
 
 
#Cod Wesley         
#import datetime 
#array1=np.arange(1000)
#array2=np.arange(1000)

#time1=datetime.datetime.now()
#list=[]
#for i in array1:
#    for j in array2:
#        x = i+j
#        print(x)
        # list.append(x)
# print(list)
#time2=datetime.datetime.now()
#print(time2-time1)


#import time
#array1=np.arange(1000)
#array2=np.arange(1000)

#tempo_inicial = time.time()
#for i in array1:
#    for j in array2:
#       x = i+j 
#        print(x)
                
#    tempo_total = time.time()
#    resultado = tempo_total - tempo_inicial
#    print(round(resultado,2))
