""" @autor: Professor Felipe """

from cassandra.cluster import Cluster
from cassandra.connection import EndPoint

class Connector:

    cluster = Cluster()
    session = cluster.connect('soulcode2')
 
    
def connect(self):
    """Database connection method
    """
    if(self.scheme == "cassandra"):
        try:
            self.client = Cluster()
            self.con = self.client.connect(self.database)
        except Exception as e:
            print("Cassandra connect error: ",str(e)) 
            
def disconnect(self, con, cursor):
        """Method for disconnecting from a relational database (Mysql or Postgresql)
        """
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print("Disconnect error: ",str(e)) 


def get_all(self, target):
    """Method to return a table or collection in pandas dataframe format
    """
    if(self.scheme == "cassandra"):
        try:
            self.connect()
            collection_data = self.con.execute(f"select * from {target};")
            list = []
            for d in collection_data:
                list.append(d)
        except Exception as e:
            print("Cassandra get all error: ",str(e)) 

            
        
# METODO PARA INSERIR
    # def Inserir(tabela, atributos, dados_a_inserir):
    #     insert = "INSERT INTO" + tabela + "(" + atributos +"{ VALUES (uuid(), " + dados_a_inserir + "};"
    #     #print(insert)
    #     session.execute(insert)


#TODO: implement fetchall() in class
    select = "SELECT * FROM alunos;"
    dados = session.execute(select)
    print(dados)
    for dado in dados:
        print(dado)
        
    def selecionar_uma(self,query):
        try:
            con, cursor = self.connect()
            cursor.execute(query)
            return cursor.fetchone() #fetchone imprimi apenas a 1 linha.
        except Exception as e:
            print(str(e))            
        finally:
            self.desconectar(con,cursor)
    
    def selecionar_tudo(self,query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))            
        finally:
            self.desconectar(con,cursor)    
        
        
    #UPDATE
    update = "UPDATE alunos SET telefone = '4589761234' WHERE matricula = '<a chave uuid()>';"
    session.execute(update)

    #DELETE
    delete = "DELETE FROM alunos WHERE matricula = '<a chave uuid()>';"
    session.execute(delete)
    
    
    
          
    def __init__(self,user,password,host,database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        
    
           
    def cadastrar(self,value): #função de cadastro com valor e que passa uma tupla.
        try:
            con, cursor = self.conectar()
            query = f"INSERT INTO cliente (nome,data_cadastro,plano,data_plano,vencimento) VALUES {tuple(value)}"
            print(query)
            cursor.execute(query)
            return 'Cliente cadastrado com sucesso!'
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con,cursor)
            
    def selecionar_uma(self,query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchone() #fetchone imprimi apenas a 1 linha.
        except Exception as e:
            print(str(e))            
        finally:
            self.desconectar(con,cursor)
    
    def selecionar_tudo(self,query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))            
        finally:
            self.desconectar(con,cursor)
