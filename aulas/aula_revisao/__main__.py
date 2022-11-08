# ESTRUTURAS CONDICIONAIS IF, ELSE, ELIF

# ESTRUTURA CONDICIONAL SIMPLES (IF) SOZINHO
    # """
    # if (expressão_se_verdadeira):
    #     executar_bloco_de_comandos()
    # """
    # idade = 42
    # if idade < 18:
    #     print("Você ainda é menor de idade!") #Nesse caso não imprima nada pq é uma condição falta, a idade é maior q 18
        
    
    # # ESTRUTURA CONDICIONAL COMPOSTA (IF, ELSE)
    # """ TRUE , FALSE
    # if (expressao_se_verdadeira):
    #     executar_bloco_de_comandos()
    # else:
    # executar_bloco_de_comando() -- false    
    # """
    # idade = 42
    
    # if idade < 18:
    #     print("Você ainda é MENOR de idade!")
    # else: 
    #     print("Você é MAIOR de idade!")
    
    
    # # ESTRUTURA CONDICIONAL ENCADEADA (IF, ELIF, ELSE)    
    # """ TRUE , FALSE
    # if (expressao_se_verdadeira):
    #     executar_bloco_de_comandos()
    # elif (expressao_se_verdadeira):
    #     executar_bloco_de_comandos()    
    # else:
    # executar_bloco_de_comando() -- false    
    # """   
    # """
    # até 11 anos é criança
    # de 12 a 17 é adolescente
    # menor que 60 é adulto
    # acima de 60 idoso
    # """  
    # idade = 42   
        
    # if idade <= 11:
    #     print("Criança")
    # elif idade > 11 and idade <=17:
    #     print("Adolescente") 
    # elif idade > 18 and idade < 60:
    #     print("Adulto")
    # else:
    #     print("Idoso")
        
        
    # # TRABALHANDO COM ESTRUTURA DE REPETIÇÃO WHILE 
    # contador = 0
    
    # while (contador <=10): # Primeiro - 0<=10... TRUE, Segundo - 1<=10... TRUE, 3...2..11 FALSE
    #     print(contador) 
    #     #contador +=1
    #     contador = contador + 1   
    
    # # Percora N em range entre O e 11    
    # for n in range(0, 11):
    #     print(n) 
    
    
    # ############
    # nomes = ["Adriano", "Felipe", "Diego", "Juliana", "Tais"]    
    
    # #percorra N em nomes e print nomes
    # for n in nomes:
    #     print(n)
    # #Se não for igual a condição de cima, então:
    # else:
    #     print("Todos os nomes foram listados com sucesso!")
        
    # ############        
    # lista = [1,2,3,4,5,6,7,8,9,10]
    
    # for numero in lista:
    #     print (numero * 2)
    
    # for numero in lista:
    #     x = numero * 2
    #     print (x)    
       
    # """ 
    # Se tiver [] = lista
    # Se tiver {} = 
    # Tupla: é definida pela ,
    # """       
    
############  
# posições:   1   ,   2   ,   3  
lista2d = [[1,2,3],[4,5,6],[7,8,9]] 
"""
indices:
externo
0 
    0.0 = 1
    0.1 = 2
    0.2 = 3
1
    1.0 = 4
    1.1 = 5
    1.2 = 6
2
    2.0 = 7
    2.1 = 8
    2.2 = 9
"""    
for externa in lista2d:
    for interna in externa:
        print("lista 2d:", interna)
        
lista3d = [[[5.0, 4.5],[2.1,6.5],[8.6,7.0]],[[4.2,5.1],[9.0,8.0],[2.3,4.4]]]
for externa in lista3d:
    for interna in externa:
        for i in interna:
            print("lista 3d", i)         
        
