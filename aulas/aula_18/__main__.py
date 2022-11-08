# ----------------------------------------------------------------------------------
# -- CRIANDO CLASSES PARA INTERAGIR UMAS COM AS OUTRAS (PRODUTOS, CLIENTES, FUNCIONARIOS, VENDAS)
# ----------------------------------------------------------------------------------
from modules.vendas import Vendas
from modules.clientes import Clientes
from modules.pessoas import Pessoa
from modules.funcionarios import Funcionarios
import time

while True:
        import os
        selecao = input("1 - CADASTRANDO PESSOAS \n"
                        "2 - CADASTRANDO FUNCIONARIOS \n"
                        "3 - CADASTRANDO CLIENTES \n"
                        "4 - EFETUANDO VENDA \n"
                        "5 - EFETUANDO CADASTRO DE PRODUTO \n"
                        "5 - ENCERRAR \n"
                        " Faça sua escolha: ")
        
                        
                        
        if selecao == '1':
            
            
            cadastro = Pessoa(pessoas=None) 
            cadastro.inserir_dados()   
            time.sleep(2)
            os.system('cls')
            

        
        if selecao == '2':
            
            
            cadastro = Funcionarios(pessoas=None)
            cadastro.inserir_dados()
            
            time.sleep(2)
            os.system('cls')
            
        
        
        if selecao == '3':
            
            cadastro = Clientes(pessoas=None)
            cadastro.inserir_dados()
            
            time.sleep(2)
            os.system('cls')
        
        
            
        if selecao == '4':
            
            cadastro = Vendas(pessoas=None)
            cadastro.inserir_dados1()
            cadastro.inserir_dados()
            
            time.sleep(2)
            os.system('cls')
            
            
        if selecao == '5':
            
            break