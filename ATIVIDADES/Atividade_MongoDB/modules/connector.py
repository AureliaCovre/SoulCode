from datetime import datetime
from pymongo import MongoClient, collection, database, results
import pymongo
from modules.funcionarios import Funcionarios
import pandas as pd


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
    
    # -- ----------------------------------------------------------
    # -- ATIVIDADE DO FELIPE EM AULA
    # -- ----------------------------------------------------------
    
    # CADASTRAR CADA FUNCIONARIO
    def inserir_muitos(self,dado):
        while True:
            selecao = input("1 - Deseja inserir um funcionario \n"
                            "2 - Encerrar \n"
                            "Faça sua escolha: ")
            if selecao == '1':
        
                    dado = []
                    a = Funcionarios(nome=None,indentifica=None)
                    a.set_nome(input("Digite o nome do funcionario: "))
                    a.set_indentifica(input("Digite o cpf do funcionario: "))
                    a.set_horas_trabalho(input("Digite as horas trabalhadas mes: "))
                    a.set_inicio_contrato(input("Digite data do inicio de contrato: "))
                    a.set_fim_contrato(input("Digite a data de fim de contrato: "))
                    a.set_quantidade_venda(input("Digite total de vendas: "))     
                    
                    dado.append({"nome_fun":a.get_nome(),"cpf":a.get_indentifica(),"horas_trabalho_mes":a.get_horas_trabalho(),"inicio_contrato": a.get_inicio_contrato(),"final_contrato":a.get_fim_contrato(),"total_venda":a.get_quantidade_venda()})
                    self.collection.insert_many(dado)
            elif selecao =='2':
                break
    
    
    # HORA EXTRA DE CADA FUNCIONARIO   
    def hora_extra(self):
        interface_mongo = Interface_db()  
        resultado = [
            {'$project': {'_id': 0,'inicio_contrato': 0, 'final_contrato': 0, 'total_venda': 0}},
            {'$match':
                {'$and':
                [
                    {'horas_trabalho_mes': {'$gt': 220}}
                    ]
                }
            }
        ]
        
        a = interface_mongo.aggregate(resultado)
        lista_horas = [220,220,220,220]
        nome_lista = []
        lista = []
        for i in a:
            nome_lista.append(i['nome_fun'])
            lista.append(i['horas_trabalho_mes'])
        
        horas_extras = []
        a = lista[0]- 220
        b = lista[1]- 220
        c = lista[2]- 220
        d = lista[3]- 220
        horas_extras.append(a)
        horas_extras.append(b)
        horas_extras.append(c)
        horas_extras.append(d)
        
        nome_lista  
        horas_extras
        x = pd.DataFrame({'nome':nome_lista, 'horas extras': horas_extras})
        print(x)
   
    
    # AS VENDAS DE CADA FUNCIONARIO POR MÊS
    def pesquisar_vendas(self):
        interface_mongo = Interface_db()
        a = interface_mongo.buscar()
        inicio,fim,valor,nome = [], [], [],[]
        
        for i in a:
            nome.append(i['nome_fun'])
            inicio.append(i['inicio_contrato'])
            fim.append(i['final_contrato'])
            valor.append(i['total_venda']) 
        
        j = int(input("Digite um numero para selecionar um funcionario: "))
        o = datetime.strptime(inicio[j], "%d-%m-%Y")
        b = datetime.strptime(fim[j], "%d-%m-%Y")
        total = b - o
        x = total.days 
        total_vendas = (valor[j]/x)*30
        print("Nome funcionario: ", nome[j])
        print("Quantidade de vendas em um mês: ", total_vendas)
        
    # O CONTRATO DO FUNCIONARIO VENCE QUANDO
    def contrato_fun(self):
        interface_mongo = Interface_db()
        a = interface_mongo.buscar()
        lista1 = []
        lista = []
        for i in a:
            lista1.append(i['nome_fun'])
            lista.append(i['final_contrato'])
            
        j = int(input("Digite um numero para selecionar um funcionario: "))
        print("Nome funcionario: ", lista1[j])
        print("O contrato dela vence em: ", lista[j])
