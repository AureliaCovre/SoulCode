import numpy as np

# Dado o array
# arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
# desenvolva um código em Python que, considerando os dados como [id do vendedor, id do cliente, total da vena] calcule e apresente:
# - qual o id do vendedor que fez o maior valor total em vendas?
# - qual o cliente que fez o maior numero de compras?
#Nessa aula vamos ver Array de mais de uma dimissão, depois pesquisar melhor o que são os array de mais de uma dimenssão.

import numpy as np

if __name__ == "__main__":
  #  try:
        #arr = np.array([[1,1,150], [1, 2, 200], [1, 3, 78], [1, 2, 50], [2, 1, 150], [2, 2, 200], [2,2,200] [2,3,78], [2,2, 50]])
        #print(arr)
    #except Exception as e:
      #  print(str(e))


        arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,5000], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
        for venda in range(len(arr)):
            print("id do vendedor: ", arr[venda][0], " id do cliente: ", arr[venda][1], " total da venda: ", arr[venda][2])
        except Exception as e:
            print(str(e))

        for i in range(len(arr)):
           if 1 == arr[i][0]:
               valor_vendas_vend1 = arr[0][2] + arr[1][2] + arr[2][2] + arr[3][2]
               id_vendedor_1 = arr[0][1]
        print(valor_vendas_vend1)

        for i in range(len(arr)):
           if 2 == arr[i][0]:
               valor_vendas_vend2 = arr[4][2] + arr[5][2] + arr[6][2] + arr[7][2]
               id_vendedor_2 = arr[4][2]
        print(valor_vendas_vend2)

        if valor_vendas_vend1 > valor_vendas_vend2:
            print("Id do vendedor que fez a maior venda é:", + id_vendedor_1)
        elif valor_vendas_vend1 == valor_vendas_vend2:
            print("O valor total das vendas dos vendedores é igual")
        elif valor_vendas_vend1 < valor_vendas_vend2:
           print("Id do vendedor que fez a maior venda é:", + id_vendedor_2)

        cliente1 = 0
        cliente2 = 0
        cliente3 = 0

        for k in range(len(arr)):
           if arr[k][1] == 1:
              cliente1 = cliente1 + 1
              print(cliente1)
           if arr[k][1] == 2:
              cliente2 = cliente2 + 1
           if arr[k][1] == 3:
              cliente3 = cliente3 + 1
        print(cliente1, cliente2, cliente3)




# arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
# vendedor1 = []
# vendedor2 = []
# for venda in arr:
#     id = arr(id[0])
#     vendedor1.append(id)
# for id in vendedor1:
#     id.apresentar 
  
#   #  print(sum(arr[venda][2]))


#  lista_alunos = []
#         for al in db_alunos:
#             aluno = alunos(al[1], al[0], al[2])
#             lista_alunos.append(aluno)

#         for aluno in lista_alunos:
#             aluno.apresentar()


# # for venda in range(len(arr)):
# #     print("id do vendedor: ", arr[venda][0], " id do cliente: ", arr[venda][1], " total da venda: ", arr[venda][2])
    
# # if 1 == arr["Select sum([venda][0])":
    
    
#     ("SELECT sum(valor_total) as total_vendas from vendas")
    
