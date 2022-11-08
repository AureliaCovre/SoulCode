# Equipe: André, Aurélia e Dani

from modules.connector import CassandraConector
import uuid
import random


cargos = ['engenheiro','arquiteto','professor','eletricista','medico','advogado','engenheiro de dados']
nomes = ['Andre','Alejandro','Aurelia','Daniele','Enzo','Adriano','Felipe','Juana','Laura','Isabella','Carla','Daniela','Leticia','Sandy']
departamento = ['RH','MARKETING','ARQUITETURA','ENGENHARIA','PROJETOS','CONSULTORIA','FINANCEIRO']
lista_dados = []

for i in range(1,5001):
    dicionario = {'num_registro':str(uuid.uuid4()),'nome_func':f"'{random.choice(nomes)} {random.choice(nomes)}'",'cargo': f"'{random.choice(cargos)}'",
     'departamento':f"'{random.choice(departamento)}'", 'salario': f'{random.randint(2000,10000)}','end_func':f"'RUA {i}'",
     'tel_func': f"'{random.randint(111111111,999999999)}'"}
    lista_dados.append(dicionario)
    
con = CassandraConector('empresa_soulcode')
con.insert(1,'funcionarios',lista_dados)    
