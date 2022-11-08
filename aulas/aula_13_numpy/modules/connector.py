import mysql.connector

class interface_db:
    usuario=""
    senha=""
    host=""
    banco="" 

    def __init__(self, usuario, senha, host, banco):
        try:
            self.usuario=usuario
            self.senha=senha
            self.host=host
            self.banco=banco
        except Exception as e:
            print(str(e))

        """[Conectar]
            Estabelece conexão com o banco
        """
    def conectar(self):
        try:
            con= mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))


        """[Desconectar]
            Desconecta do banco
        """
    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
    
        """[Método selecionar]
            args:
            query string: recebe a query pronta completa
            o_que string: recebe os campos a serem selecionados
            de_onde string: recebe a tabela em que vai ser feito a consulta
            argumento string: recebe o argumento da consulta
        """
    def selecionar(self, o_que, de_onde, argumento):
        try:
            con, cursor = self.conectar()
            query="SELECT "+o_que+" FROM "+de_onde+argumento+";"
            cursor.execute(query)
            for row in cursor:
                print(str(row))
            return cursor.fetchall()            
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

        """[Método inserir]
            args:
            tabela string: recebe a tabela que vai ser feito o insert
            atributo string: recebe os campos a serem feitos os inserts
            valor string: recebe os valores aos quais serão feitos os inserts
        """
    def inserir(self, tabela, atributo, valor):
        try:
            con, cursor = self.conectar()
            query="INSERT INTO "+tabela+atributo+" VALUES("+valor+");"
            cursor.execute(query)
            con.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

        """[Método delete]
            ? faz sentido esse método para fazer o que o cliente pediu
        """
    def delete(self, tabela, atributo):
        try:
            con, cursor = self.conectar()
            query= "DELETE FROM "+tabela+" WHERE "+atributo
            cursor.execute(query)
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def totalVendas(self):
        try:
            con, cursor = self.conectar()
            query = "SELECT SUM(valor_total) FROM venda;"
            cursor.execute(query)
            return cursor.fetchall()[0][0]
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def maiorVenda(self):
        try:
            con, cursor = self.conectar()
            query = "SELECT v.nome, ven.valor_total FROM vendedor v, venda ven WHERE v.id_vendedor = ven.id_vendedor AND ven.valor_total IN(SELECT MAX(valor_total) FROM venda WHERE valor_total);"
            cursor.execute(query)
            return cursor.fetchall()[0]
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def maiorQuantidadeDeVendas(self):
        try:
            con, cursor = self.conectar()
            query = "SELECT r.nome, COUNT(v.id_vendedor) as quantidade_vendas FROM vendedor r, venda v WHERE r.id_vendedor=v.id_vendedor GROUP BY r.nome ORDER BY quantidade_vendas DESC limit 1;"
            cursor.execute(query)
            return cursor.fetchall()[0]
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def fornecedorMaisUtilizado(self):
        try:
            con, cursor = self.conectar()
            query = "select f.nome, count(v.id_produto) from fornecedor f, produto p, venda v where f.id_fornecedor =  p.id_fornecedor and p.id_produto = v.id_produto group by f.nome order by count(v.id_produto) desc limit 5;"
            cursor.execute(query)
            return cursor.fetchall()[0]
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def comissao(self):
        try:
            con, cursor = self.conectar()
            query = "SELECT vendedor.nome, SUM(venda.valor_total * (venda.comissao/100)) FROM vendedor INNER JOIN venda ON vendedor.id_vendedor = venda.id_vendedor GROUP BY  vendedor.nome ORDER BY vendedor.nome;"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
