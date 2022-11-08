from modules.connector import conectar
from modules.item import Item

    
if __name__ == "__main__":
    # Conectando a base de dados
    database = conectar()
    # Criando a collection
    collection_name = database['client']
    
    # item = {'nome': 'teste', 'cpf': 'teste'}
    # collection_name.insert_one(item) 
    
    
    # Criando a lista
    lista = []
    
    # Criando os objetos
    item1 = Item("Aurelia", "123.123.123-00").trazer_dicionario()
    item2 = Item("Felipe", "333.333.333-00").trazer_dicionario()
    item3 = Item("Adriano", "444.333.333-00").trazer_dicionario()
    item4 = Item("item4", "444.333.333-00").trazer_dicionario()
    item5 = Item("item5", "444.333.333-00").trazer_dicionario()
    item6 = Item("item6", "444.333.333-00").trazer_dicionario()
    item7 = Item("item7", "444.333.333-00").trazer_dicionario()
        
    # Lista de dicionarios
    lista.append(item1)
    lista.append(item2)
    lista.append(item3)
    
    # Collection_name.insert_many(lista)
    
    item_details = collection_name.find() #item_details é uma variável que vai receber a "query" lá do mongodb
    
    lista2 = []  #aí você cria uma lista vazia para receber essa consulta no mongoDB
    
    for item in item_details: #cria um laço for para ele passar por cada item lá na consulta do banco
        nome = item['nome']   #aí quando ele encontrar um nome lá na lista, ele vai guardar nessa variável nome
        cpf = item['cpf']     #do mesmo jeito aqui, só que ele vai guardar quando passar por cpf 
        x = Item(nome,cpf)    #aqui a gente junta tanto o nome quanto o cpf numa só variável
        lista2.append(x)      #daí a gente adiciona essa variavel x (que juntou o nome, e o cpf), na lista vazia que a gente criou lá em cima
                
    for i in lista2:    #aí aqui a gente faz outro for, pra pecorrer a lista que a gente acabou de fazer (linha 30)
        print(i.get_nome(), i.get_cpf())    #usando os gets, a gente traz o nome e o cpf da lista2
        
    
    for j in range(len(lista2)):    # Printando a quantidade de linhas que tem na lista 2
        print(j)
        
    for j in lista2: # Printando os objetos da lista
        print(j)  
        
    lista_cpf_novos = ['333.333.333-33','444.444.444-44','555.555.555-55'] 
    
    for i, j in zip(lista2, lista_cpf_novos): #zip: junta as duas listas. O i é o indice do CPF da lista2 e o J o indice CPF da lista novos
        collection_name.update_one({"cpf": i.get_cpf()}, {"$set":{"cpf": j}}) #fazendo o update    
        print(i.get_cpf(),j)  #printa o cpf antigo e o novo
        
        # A parte do update https://www.geeksforgeeks.org/python-mongodb-update_one/
        
    # Deletando um elemento usando o deleteOne
    collection_name.delete_one({"nome": "teste"}) #Aqui ele esta deletando todos os elementos com nome: teste
    new_details=collection_name.find()   # Select * from client
    
    for i in new_details:
        print(i["nome"],i["cpf"])   
