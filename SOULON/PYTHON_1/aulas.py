# #-- -------------------------------------------------------------------------------------
# # AULA 6 - ESTRUTURAS DE LISTA
# #-- -------------------------------------------------------------------------------------

# """ 6.3 - FATIANDO LISTAS"""

# #indice= 0 1 2
# lista = [2,3,4]
# #       -3-2-1

# nova_lista = lista[0]      #Imprime o 2
# nova_lista = lista[0:2]    #Imprime = 2,3 , pq o indice 2 ele não considera
# nova_lista = lista[0:2:2]  #Imprime = 2, pq ele esta saltando de dois em dois indices e nessa lista só tem 3 elementos
# #print(nova_lista)

# lista2 = ['p', 'y','t','h','o','n']
# nova_lista2 = lista2[::-1]   #Imprime a lista de traz pra frente
# #print(nova_lista2)


# """ 6.4 - EXERCÍCIO PRÁTICO """
# lista3 = ['P','Y','T','H','O','N']
# nova_lista3 = lista3[3:6]
# #print(nova_lista3)


# """ 6.5 - INCLUIR, ALTERAR, EXCLUIR ELEMENTO DE LISTAS """
# animais = ['Gato', 'Cachorro', 'Elefante']
# #print(animais)
# animais.append('Galinha')       # APPEND - Adiciona ao final da lista
# animais.insert(0,'Papagaio')    # INSERT - Adiciona no indice que você escolher
# animais.pop(0)                  # Comando POP - Remove o indice que você escolher
# animais.remove('Gato')          # Comando REMOVE - Remove o elemento pelo nome que você escolher
# #print(animais)


# """ 6.6 - ORDENAR LISTAS """
# lista_ordenar = ['a','x','s','w','d','a','n','a']
# lista_ordenar.reverse()   #Comando para reverter a ordem da lista
# lista_ordenar.sort()      # Comando para ordenar a lista

  
# #for i in range(len(lista_ordenar)):  #percorrendo o tamanho da lista
#     #print(lista_ordenar[i])
    
# l = lista_ordenar.count('a')    #Comando COUNT - para contar quantos elementos dentro do parenteses tem na lista
# #print(l)    

# """ 6.7 - EXERCÍCIO PRÁTICO """
# lista_moveis = ['cama', 'mesa','sofá','cadeira']
# lista_moveis.append('prato')
# lista_moveis.pop(2)
# #print(lista_moveis)

# #-- -------------------------------------------------------------------------------------
# # AULA 7 - ESTRUTURA DE TUPLAS
# #-- -------------------------------------------------------------------------------------
# """ 7 -  INTRODUÇÃO A TUPLAS """
#     ### A tupla é imutavel!
#     ### Quando temos parenteses seguidos de virgula temos uma tupla

# t = tuple("abc")
# x = ("python", "curso")  # Elementos do tipo string    
# x1 = (2,3,4)             # Elementos do tipo inteiro
# x2 = (2.5,1.6,4.8)       # Elementos do tipo float
# x3 = ("python", 1, 4.5, True)     # Tupla mista, (True é variavel boleana)
# #print(x3)
# #print(type(x3))    #Comando TYPE para verificar o tipo de dados que temos aqui , nesse caso class 'tuple'


# """ 7.1 - OPERAÇÕES COM TUPLAS """
# elementos_tupla = ('São Paulo', 'Belo Horizonte', 'Teresina')
# # print('Teresina' in elementos_tupla) # Verificando se Teresina existe dentro da tupla

# nomes_tuplas = ('José', 'Carlos', 'Maria', 'Pedro','Maria', 'Joana','Maria')
# # print(nomes_tuplas.count('Maria')) # Contando quantos itens temos com nome Maria
# # print(nomes_tuplas.index('Carlos')) # Verificando que indice o Carlos esta


# #-- -------------------------------------------------------------------------------------
# # AULA 8 - ESTRUTURA DE DICIONARIO
# #-- -------------------------------------------------------------------------------------
# """ 8 -  INTRODUÇÃO A DICIONÁRIOS """
#     ### Os dicionarios são estruturas de dados interessantes pq podemos escolher/ definir as chaves, não precisamos deixar que 
#         # o sistema insete pra gente essa chave de acesso. Além de que eles podem armazenar outras estruturas de dados
#          # dentro dele.

#           #{chave:valor, chave: valor}         
# dicionario = {"a":"amor", "b":"blue"}                #dicionario com elementos tipo stg 
# dicionario2 = {1:20, 3:30, 4:40}                     #dicionario com elementos tipo inteiro
# dicionario3 = {5.5:50.50, 30.1:30.25}                #dicionario com elementos tipo float 
# dicionario4 = {(10,20):["python", "linguagem", 10]}  # tupla como chave e o valor dessa chave pode ser uma lista

# # print(dicionario)
# # print(type(dicionario)) # Imprimindo o tipo (class 'dict')

# """ 8.1 -  ACESSANDO DICIONARIOS """ ##### ERRO

# """ 8.2 -  FUNÇÕES COM DICIONARIOS """ 
#     ### dicionarios são mutaveis

#     #aqui estamos dizendo que esse numero de tefone pertence ao nome da frente do numero    
# agenda = {4040021:"José", 87541236:"Heloise", 78945612:"Carlos", 36925874:"Claudio"}    
# # print(agenda)
# #del(agenda[4040021]) # DEL - Elimina o elemento do dicionario pela chave informada
# # print(agenda)

# # print(agenda.keys())   # Imprime apenas as chaves
# # print(agenda.values()) # Imprime apenas os valores
# # print(len(agenda))
# # print(agenda.popitem()) # Remove o ultimo item e imprime qual elemento foi removido

# """ 8.3 - EXERCÍCIOS  """ 
# ### 1-Crie um dicionário contendo dias da semana sendo dia1, dia2, dia3...as chaves e o dia seu valor. Ex: “dia1”: “domingo”.
# ### 2-Remova dois dos últimos dias da semana.
# ### 3-Remova segunda-feira pela sua chave.
# ### 4-Imprima chaves e valores do dicionário.5-Imprima o dicionário final.

# dicionario_semana = {"DIA1":"Domingo", "DIA2":"Segunda", "DIA3":"Terça", "DIA4":"Quarta",
#                      "DIA5":"Quinta","DIA6":"Sexta", "DIA7":"Sábado"}
# # print(dicionario_semana.popitem())
# # print(dicionario_semana.popitem())
# # del(dicionario_semana["DIA2"])
# # print(dicionario_semana.keys())
# # print(dicionario_semana.values())
# # print(dicionario_semana)


# #-- -------------------------------------------------------------------------------------
# # AULA 9 - FUNÇÕES
# #-- -------------------------------------------------------------------------------------
# """ 9 - INTRODUÇÃO A FUNÇÕES  """ 

# def funcao():
#     print("Eu sou uma função!")

# """ 9.1 - PARÂMETROS DE FUNÇÕES  """  
  
# def somar(x, y):
#     total = x + y 
#     #print(total)
    
# somar(10, 20)

# """ 9.2 - RETORNO DE VALORES  """  
# def show():
#     return 15

# #print(show())  

# def mult(a,b):
#     return a * b

# #print(mult(2,5))

# """ 9.3 - EXERCÍCIO PRÁTICO  """  
#     ### 1-Crie uma função que receba dois parâmetros e realize sua soma,subtração, adição e multiplicação.
#     ### 2-Informe esses resultados através de um print ao usuário dentro da função

# def operacoes (x, y):
#     soma = x + y
#     sub = x - y
#     div = x / y
#     multp = x * y
 
#     # print("Soma: ", soma)
#     # print("Subtração: ", sub)
#     # print("Divisão: ", div)
#     # print("Multiplicação: ", multp)    
  
# operacoes(15, 25)      

#-- -------------------------------------------------------------------------------------
# AULA 10 - PROJETO FINAL
#-- ------------------------------------------------------------------------------------- 
""" 1-Deve se criar 5 funções diferentes,sendo elas somar,subtrair,dividir,multiplicar e listar.
    2-Deve se criar um MENU com if else sendo que o usuário escolha qual função deve acessar.
    3-Ao ser escolhido a função,o usuário é direcionado a ela e insere os parâmetros que desejam realizar as operações.
    4-As funções matemáticas devem receber os números para realizar a operação, realizar o cálculo e imprimir o resultado
    para o usuário.
    5- Na função listar,deve-se criar uma lista de vantagens do python e imprimir para o usuário.
"""
import time
import os


def somar_1():
    a = int(input("Digite o valor desejado: "))
    b = int(input("Digite o valor desejado: "))
    print("A resultado da soma é: ", a + b)
           
def subtrair():
    a = int(input("Digite o valor desejado: "))
    b = int(input("Digite o valor desejado: "))
    print("A resultado da subtração é: ", a - b)
    
def dividir():
    a = int(input("Digite o valor desejado: "))
    b = int(input("Digite o valor desejado: "))
    print("A resultado da divisão é: ", a / b)
    
def multiplicar():
    a = int(input("Digite o valor desejado: "))
    b = int(input("Digite o valor desejado: "))
    print("A resultado da multiplicação é: ", a*b)    

def listar():
    lista = ("Além da simplicidade e de permitir um aprendizado veloz aos iniciantes,\n o Python destaca- se pela robustez, por se comunicar com outros \n sistemas ou linguagens e por ser multiplataforma, utilizada em sistemas Linux, Mac OS ou Windows")   
    print(lista)

while True:
    os.system('cls')
    # print("Seleciona a opção desejada: 1 - Soma  2 - Subtração  /n3 - Divisão  /n4 - Multiplicação  /n5 - Lista ")
    selecao = input("Seleciona a opção desejada: \n"
                    "1 - Soma\n" 
                    "2 - Subtração\n"
                    "3 - Divisão\n"
                    "4 - Multiplicação\n"
                    "5 - Vantagens do PYTHON:\n ")  
          
    if selecao == "1":
        somar_1()
        time.sleep(4)
    elif selecao == "2":
        subtrair()
        time.sleep(4)
    elif selecao == "3":
        dividir()
        time.sleep(4)
    elif selecao == "4":
        multiplicar()
        time.sleep(4)
    elif selecao == "5":
        listar()
        time.sleep(4)    
    else:
        break    

