from modules.connector import Interface_db


if __name__ == "__main__":
   
   
   interface_mongo = Interface_db()
   
   while True:
          
            selecao = input("1 - INSERIR FUNCIONARIO \n"
                          "2 - PESQUISAR VENDAS DO MÊS \n"
                          "3 - HORA EXTRA \n"
                          "4 - QUANDO CONTRATO VAI ENCERRAR \n"
                          "Faça sua escolha: ")
   
            
            # INSERINDO FUNCIONARIOS
            if selecao == '1':
               
               interface_mongo.inserir_muitos(dado=None)
                  
            
            # PESQUISANDO AS VENDAS VIA MÊS DE CADA FUNCIONARIO
            elif selecao =='2':      
               
               interface_mongo.pesquisar_vendas()
                  
            
            # HORA EXTRA
            elif selecao == '3':
               
               interface_mongo.hora_extra()
                  
            # CONTRATO ENCERRANDO ESSE MÊS
            elif selecao == '4':
                   
               interface_mongo.contrato_fun()
   
    
   # INSERIR DADOS NO BANCO
   # query = {'nome':'Bruno'}
   # interface_mongo.inserir(query)
     
   # COMO DELETAR ALGO NO BANCO
   # interface_mongo.deletar({'nome':'test'})
  
   # BUSCA NO BANCO NOSQL
   # print(interface_mongo.buscar())
   
   # UPDATE COMPLETO NO BANCO
   # dado = {'nome':'tese'}
   # dados = { '$set': {'nome': 'Bruno'}}
   
   # interface_mongo.update()
   
   # print(interface_mongo.buscar())
   
   # # AGREGATE COMPLETO NO BANCO NOSQL
   # resultado = [
	# {'$match': {'quant_like': {'$ne': 0}}},
	# {
	# '$group': {'_id': "$titulo_posta",
	# 'media_likes': {'$avg': "$quant_like"},
	# }
	# },{'$sort': {'media_likes': 1}}]
   
   # interface_mongo.aggregate(resultado)
