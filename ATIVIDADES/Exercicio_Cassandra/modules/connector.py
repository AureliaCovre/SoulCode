__author__ = "André Ventura"

from cassandra.cluster import Cluster

class CassandraConector:
    
    def __init__(self,keyspace:str):
        self.cluster = Cluster()
        self.session = self.cluster.connect(keyspace)
        
    def insert(self,tipo:int=0,familia:str='',dicionarios=''):
        
            for dicionario in dicionarios:
                keys = list(dicionario.keys())
                values = list(dicionario.values())
                query = f"INSERT INTO {familia} ({','.join(keys)}) VALUES ({','.join(values)});"
                # print(query)
                self.session.execute(query)
               
            print('inseridos',len(dicionarios))
