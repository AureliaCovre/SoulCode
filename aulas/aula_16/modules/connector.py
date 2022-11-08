from pymongo import MongoClient

""" Cada cliente só acessa um banco"""


# def conectar(): #conector simples
#     client = MongoClient("mongodb://127.0.0.1:27017/")
#     return client['teste']

class Interface_db:
    #Atributos
    client = ""
    database = ""
    collection = ""
    
    """ Aqui conecta um banco de dados"""
    # def __init__(self):
    #     #aqui estou dizendo que o atributo cliente contém o mongo cliente
    #     self.client = MongoClient("mongodb://127.0.0.1:27017/")
    
    """ Assim podemos conctar varios bancos"""
    def _init_(self, host = "mongodb:// 127.0.0.1: 27017"):
        self.client = MongoClient(host) #client é para estabelecer a conexão
        self.set_database()
        self.set_collection()
        
    def set_database(self, database="test"):
        self.database=self.client[database] 
        
    def set_collection(self, collection="professores"):
        self.collection = self.database[collection]
        
    def buscar(self):
        self.collection.find()
