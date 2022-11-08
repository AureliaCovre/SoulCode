from typing import Match
from pymongo import results
from modules.connector import Interface_db
import pymongo
import array as np

# Crie uma classe funcionario, instancie 5 funcionarios, calcule e apresente para cada funcionario:
#- quantas horas extras que cada funcionario fez neste mes
#- o total de vendas neste mes para cada funcionario
#- se o contrato do funcionário se encerra neste mes

if __name__ == "__main__":
   interface_mongo = Interface_db()
   cadastro = Funcionarios(nome=None, indentifica=None)
   
   # BUSCA NO BANCO NOSQL
   # print(interface_mongo.buscar())
      
   # {"nome_fun":"Desi",
   # "cpf":"773653211-7",
   # "horas_trabalho_mes":236,
   # "inicio_contrato":new Date(2021,10,28),
   # "final_contrato":new Date(2021,12,30),
   # "total_venda":5723.10}])
   # quantas horas extras que cada funcionario fez neste mes
   # AGREGATE COMPLETO NO BANCO NOSQL
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
   print(horas_extras)
   
   mergedlist = l
   
   
#    db.professor.aggregate( 
# 	[ 
# 		{$project: {_id:0}}, 
# 		{$match: 
# 			{$and: 
# 				[
# 				{categoria: "Pleno"},{avaliacao:{ $gte:6}}, {avaliacao:{$lte:8}}
# 				]
# 			} 
# 		} 
# 	]
# ).pretty()
