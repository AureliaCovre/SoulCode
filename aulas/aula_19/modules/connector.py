from cassandra.cluster import Cluster

cluster = Cluster()
session=cluster.connect('soulcode2')
# query = "INSERT INTO alunos (matricula, nome, endereco, telefone, curso) VALUES (uuid(), 'teste', 'rua X', '123123123', 'Engenharia de dados');"
# #print(query)
# session.execute(query)

#Select do Teles:
# select_table = "select * from alunos"
# result = session.execute(select_table)
# for i in result:
#     print(i)

#READ
#TODO: implement fetchall() in class
query = "SELECT * FROM alunos;"
dados = session.execute(query)
for dado in dados:
    print(dado)
    
    
#UPDATE
query1 = "UPDATE alunos set endereco = 'Avenida H' where matricula =  fa81b625-6aa3-4eb0-ad5a-213c904645e7"
query2 = "UPDATE alunos set telefone = '9999-9999' where matricula = fa81b625-6aa3-4eb0-ad5a-213c904645e7"
query3 = "UPDATE alunos set nome = 'JUBISCREUZA' where matricula = fa81b625-6aa3-4eb0-ad5a-213c904645e7"
session.execute(query1)
session.execute(query2) 
session.execute(query3)   

#DELETE
