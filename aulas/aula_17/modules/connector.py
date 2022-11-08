from pymongo import MongoClient, collection, database, results
import pymongo

class Interface_db:
    client = ""
    database = ""
    collection = ""
    dado = []
    
    def __init__(self, host="mongodb://127.0.0.1:27017/"):
        self.client = MongoClient(host)
        self.set_database()
        self.set_collection()
    
    def set_database(self, database="delloite"):
        self.database=self.client[database]
        
    
    def set_collection(self, collection="funcionarios"):
        self.collection = self.database[collection]
    
    
    def buscar(self):
        lista = []
        dados = self.collection.find()
        for d in dados:
            lista.append(d)
        return lista
    
    
    def inserir(self, dado):
        self.collection.insert_one(dado)
        print("Deu certo sua inserção!!")
    
    
    def inserir_muitos(self, dado):
        self.collection.insert_many(dado)
        
        
    def deletar(self, dado):
        self.collection.delete_many(dado)
    
    
    def update(self,dado, dados):
        self.collection.update_many(dado, dados)
        
    def aggregate(self, args):
        lista = []
        result = self.collection.aggregate(args)
        
        for i in result:
            lista.append(i)
        return lista
