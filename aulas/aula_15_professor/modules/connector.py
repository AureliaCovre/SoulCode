from pymongo import MongoClient

class Interface_db:
    client = ""
    database = ""
    collection = ""
    
    def __init__(self, host="mongodb://127.0.0.1:27017/"):
        self.client = MongoClient(host)
        self.set_database()
        self.set_collection()
    
    def set_database(self, database="soulcode"):
        self.database=self.client[database]
        
    def set_collection(self, collection="clientes"):
        self.collection = self.database[collection]
    
    def buscar(self):
        lista = []
        dados = self.collection.find()  
        for d in dados:
            lista.append(d)
        return lista
    
    def inserir_um(self, dados):
        self.collection.insert_one(dados) 
        
    def inserir_varios(self, dados):
            self.collection.insert_many(dados)       
        
    def excluir_um(self, regra):
        self.collection.delete_one(regra)  
         
    def excluir_varios(self, regra):
        self.collection.delete_many(regra) 
        
    def atualizar_um(self, regra, novo_dado):
        self.collection.update_one(regra,novo_dado)   
        
    def atualizar_varios(self, regra, novo_dado):
        self.collection.update_many(regra,novo_dado)       
            
        
    # collection_name.delete_one({"nome": "Adriano"})
    # new_details = collection_name.find() select * from client
    
    # for i in new_details:
    #     print (i['nome'], i['cpf'])
    
    # #3. deletar vários dados com o delete Many    
    # collection_name.delete_Many({"nome": "Adriano"})
    # new_details2 = collection_name.find()
    
    # for i in new_details2:
    #     print (i['nome'], i['cpf'])
    
    
