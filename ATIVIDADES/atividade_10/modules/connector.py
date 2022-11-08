import mysql.connector

class interface:
    user = ""
    password = ""
    host = ""
    database = ""
    
    def __init__(self, user, password, host, database):
        """Construtor da classe interface

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
            con = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.database)
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
    
    def inserir(self, venda, produto, quantidade): #Definindo a função de inserir as vendas
        try:
            con, cursor = self.conectar()
            valores = "({}, \"{}\", {});".format(venda, produto, quantidade)
            query = "INSERT INTO itensvenda(venda, produto, quantidade) VALUES " + valores
            cursor.execute(query)
            #print(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função inserir:", str(e))
        finally:
            self.desconectar(con, cursor)
    
    def selecionar(self, o_que, de_onde, argumentos): #Definindo a função de selecionar a venda  no banco
        try:
            con, cursor = self.conectar()
            query = "SELECT " + o_que + " FROM " + de_onde + argumentos + ";"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
    def deletar(self, codvenda): #Definindo a função de deletar vendas
        try:
            con, cursor = self.conectar()
            query = "DELETE FROM itensvenda WHERE venda = " + codvenda + ";"
            cursor.execute(query)
            #print(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função deletar na classe interface_db:", str(e))
        finally:
            self.desconectar(con, cursor)
                                     
    def executar(self, query): #Executador das querys   
        try:
            con, cursor = self.conectar()
            result = cursor.execute(query)
            return result
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
    def update(self): #Função de update da trigger na tabela itensvenda
        try:
            con, cursor = self.conectar()
            query = "CREATE TRIGGER tgr_itensvenda_Insert AFTER INSERT ON itensvenda FOR EACH ROW BEGIN UPDATE produtos SET estoque = estoque - new.quantidade WHERE referencia = new.produto; END;"
            print(query)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função trigger_update",str(e))
        finally:
            self.desconectar(con, cursor)
            
    def apagar(self): #Função de delete da trigger na tabela itensvenda
        try:
            con, cursor = self.conectar()
            query = "CREATE TRIGGER tgr_itensvenda_delete after delete on itensvenda for each row begin update produtos set estoque = estoque + old.quantidade where referencia = old.produto; END;"
            print(query)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função trigger_delete", str(e))
        finally:
            self.desconectar(con, cursor)
