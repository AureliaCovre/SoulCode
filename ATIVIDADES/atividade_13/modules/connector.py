import psycopg2

#classe com as conexoes no banco de dados 
class Interface_db:
    user = ""
    password = ""
    host = ""
    database = ""
    
    def __init__(self, user, password, host, database):
        """Construtor da classe interface_db

        Args:
            user (string): usuário para acesso ao banco de dados
            password (string): senha do usuario para acesso ao banco de dados
            host (string): string contendo o endereço do banco de dados
            database (string): srtrin contendo o nome do banco de dados
        """
        try:
            self.user = user
            self.password = password
            self.host = host
            self.database = database
        except Exception as e:
            print("ERRO no construtor:", str(e))
            
    def conectar(self):  #Definindo a função de conexão com banco
        try:
            con = psycopg2.connect(user = self.user, password = self.password, host = self.host, database = self.database)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print("ERRO na função conectar:", str(e))
            
    def desconectar(self, con, cursor): #Definindo a função de desconectar com banco
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print("ERRO na função desconectar:", str(e))
    
    
    def selecionar(self, query): #Definindo a função de selecionar e gerar a query
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
  
                                       
    def executar(self, query): #metodo para executar a inclusao, alteração e exclusão de dado  
        try:
            con, cursor = self.conectar()
            result = cursor.execute(query)
            con.commit()
            return result
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            

#funcao para as informacoes necessarias para acesso ao banco de dados
def get_db_info():
    try:
        user = "postgres"
        password = "admin"
        host = "127.0.0.1"
        database = "ATIVIDADE 13"
        return user, password, host, database
    except Exception as e:
        print(str(e))
