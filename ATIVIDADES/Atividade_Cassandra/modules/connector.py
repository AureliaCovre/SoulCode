from cassandra.cluster import Cluster

class ConexaoCassandra:

    cluster = ""
    session = ""
    
    # clstr=Cluster()
    # session=clstr.connect('soulcode')

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect('soulcode')
        
    # def conectar(self):
    #     self.cluster = Cluster()
    #     self.session = self.cluster.connect('soulcode')


    def inserir(self, tabela, atributos, dados):
        try:
            query = "INSERT INTO "+tabela+" ("+atributos+") VALUES ("+dados+");"
            self.session.execute(query)
        except Exception as e:
            print(str(e))
            
    def select(self):
        try:
            query = "SELECT * FROM alunos;"
            retorno_query = self.session.execute(query)
            for i in retorno_query:
                print(i)
        except Exception as e:
            print(str(e))
        

# -------------------------------------
# -------------------------------------

# MÉTODO PARA ATUALIZAR/FAZER UPDATE

# index_where = "CREATE INDEX ON soulcode.alunos(endereco);"
# session.execute(index_where)
# update = "UPDATE alunos SET curso = 'Matematica' WHERE endereco = 'Rua B'"
# session.execute(update)


# -------------------------------------
# -------------------------------------

# MÉTODO PARA BUSCAR/SELECIONAR
# TODO: implementar fetchall() in class
# select = "SELECT * FROM alunos"
# dados_select = session.execute(select)
# for linha in dados_select:
#     print(linha)
    
    
# -------------------------------------
# -------------------------------------

# MÉTODO PARA BUSCAR/FAZER SELECT USANDO CLÁUSULA WHERE
# index_where = "CREATE INDEX ON soulcode.alunos(telefone);"
# session.execute(index_where)
# select = "SELECT nome, endereco FROM alunos WHERE telefone = '1245565465'"
# dados_select = session.execute(select)
# for linha in dados_select:
#     print(linha)
    

# -------------------------------------
# -------------------------------------

# MÉTODO PARA DELETAR
# delete = "DELETE FROM soulcode.alunos WHERE nome = 'Joyce' ALLOW FILTERING;"
# session.execute(delete)
