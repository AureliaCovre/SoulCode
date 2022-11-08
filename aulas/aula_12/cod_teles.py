import numpy as np


arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], 
                
                [1, 2, 50], [2, 1, 150], [2, 2, 200], 
                
                [2, 3, 78], [2, 2, 50]])

array_contador = np.zeros(len(arr))
                        
contador, index, maior, maior_cliente, id_vendedor = 0,0,0,0,0

for i in range(len(arr)):
    if arr[i][2] > maior:
        maior = arr[i][2]
        
for i in range(len(arr)):
    if arr[i][2] == maior:
        print(f"id_vendedor -> {arr[i][0]} com o valor -> {maior}")
        
print(array_contador)

for i in range(len(arr)):
    array_contador[arr[i][1]] += 1

print(array_contador)

for i in range(len(array_contador)):
    if array_contador[i] > maior_cliente:
        maior_cliente = array_contador[i]
        index =  i    
               
print(index)