from modules.connector import interface_db
import numpy as np

if __name__ == "__main__":
    try:
        #array para armazenar varias notas de um aluno, possui 1 dimensao
        arr_1D = np.array([72,75,81,99,45])
        print("NOTAS do aluno")
        for nota in range(len(arr_1D)):
            print("nota na posicao ", nota, " a nota e: ", arr_1D[nota])
            
        #array para armazenar varias notas de varios alunos, possui 2 dimensoes
        arr_2D = np.array([[72,75,81,99,45], [66,76,81,95,0]])
        print("NOTAS dos alunos de uma turma")
        for aluno in range(len(arr_2D)):
            print("NOTAS do aluno : ", aluno)
            for nota in range(len(arr_1D)):
                print("nota na posicao ", nota, " a nota e: ", arr_2D[aluno][nota])
        
    except Exception as e:
        print(str(e))
        
        
# if __name__ == "__main__":
#     try:
#         arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
#         for venda in range(len(arr)):
#             print("id do vendedor: ", arr[venda][0], " id do cliente: ", arr[venda][1], " total da venda: ", arr[venda][2])            
#     except Exception as e:
#         print(str(e))       
