[11:06, 25/11/2021] +55 11 98301-2612: #Nessa aula vamos ver Array de mais de uma dimissão, depois pesquisar melhor o que são os array de mais de uma dimenssão.

import numpy as np

if __name__ == "__main__":
  #  try:
        #arr = np.array([[1,1,150], [1, 2, 200], [1, 3, 78], [1, 2, 50], [2, 1, 150], [2, 2, 200], [2,2,200] [2,3,78], [2,2, 50]])
        #print(arr)
    #except Exception as e:
      #  print(str(e))
      
      

        arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
        #for venda in range(len(arr)):
           # print("id do vendedor: ", arr[venda][0], " id do cliente: ", arr[venda][1], " total da venda: ", arr[venda][2])
    #except Exception as e:
        #print(str(e))

        total_clientes = [0,0,0]
        total_vendedores = [0,0]

        #qual o id do vendedor que fez o maior valor total em vendas
        for i in range(len(arr)):
           if 1 == arr[i][0]:
               total_vendedores[0] += arr[i][2] 
               id_vendedor_1 = arr[0][0]
           elif 2 == arr[i][0]:
               total_vendedores[1] += arr[i][2]
               id_vendedor_2 = arr[4][0]

        if total_vendedores[0] > total_vendedores[1]:
            print("Id do vendedor que fez a maior venda é:", + id_vendedor_1, "\n")
        elif total_vendedores[0] == total_vendedores[1]:
            print("O valor total das vendas dos vendedores é igual")
            print("O id dos vendedores é:", id_vendedor_1, id_vendedor_2, "\n")
        elif total_vendedores[0] < total_vendedores[1]:
           print("Id do vendedor que fez a maior venda é:", + id_vendedor_2, "\n")


        
      #   total_clientes = [0,0,0]

      #   for i in range(len(arr)):
      #      if 1 == arr[i][1]:
      #          total_clientes[0] += arr[i][2] 
      #      elif 2 == arr[i][1]:
      #          total_clientes[1] += arr[i][2]
      #      elif 3 == arr[i][1]:
      #         total_clientes[2] == arr[i][2]

      #   print(total_clientes[0], total_clientes[1], total_clientes[2])

        cliente1 = 0
        cliente2 = 0
        cliente3 = 0

        for k in range(len(arr)):
           if arr[k][1] == 1:
              cliente1 = cliente1 + 1
           if arr[k][1] == 2:
              cliente2 = cliente2 + 1
           if arr[k][1] == 3:
              cliente3 = cliente3 + 1
            
        cliente_maior_compra = max(cliente1, cliente2, cliente3)

        if cliente1 == cliente_maior_compra:
           print("O cliente 1 fez o maior numero de compras")
        elif cliente2 == cliente_maior_compra:
           print("O cliente 2 fez o maior numero de compras")
        elif cliente2 == cliente_maior_compra:
           print("O cliente 2 fez o maior numero de compras")
        elif cliente3 == cliente_maior_compra:
           print("O cliente 3 fez o maior numero de compras")



      # arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
      #   total_vendendores = [0, 0]
      #   total_clientes = [0, 0, 0]
      #   for i in range(len(arr)):
      #       if arr[i][0] == 1:
      #         total_vendendores[0] += arr[i][2]
      #       elif arr[i][0] == 2:
      #          total_vendendores[1] += arr[i][2]
      #       if arr[i][1] == 1:
      #           total_clientes[0] = total_clientes[0] + arr[i][2]
      #       elif arr[i][1] == 2:
      #           total_clientes[1] += arr[i][2] 
      #       elif arr[i][1] == 3:
      #           total_clientes[2] += arr[i][2]
      #           print("Total clientes: ", total_clientes)
      #           print("Total vendedores: ", total_vendendores)


#Nati Soulcode: cliente_maior_compra = max(total_clientes[0], total_clientes[1], total_clientes[2])
        id_maior_compra = 0
        
        for i in range(len(arr)):
            if cliente_maior_compra < arr[i][2]:
               cliente_maior_compra =  arr[i][2]
               id_maior_compra =  arr[i]             
     
        print("O cliente que efetuou a maior compra foi: ", id_maior_compra)