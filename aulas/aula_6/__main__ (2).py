import mysql.connector

def executar(query):#INSERT. UPDATE. DELETE
   try:
      con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='boa_saude')
      cursor = con.cursor()
      cursor.execute(query)
      cursor.close()
      con.commit()
      con.close()
   except Exception as e:
    print(e)

def buscar(query):#SELECT
    try:
      con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='boa_saude')
      cursor = con.cursor()
      cursor.execute(query)
      return cursor.fetchall()
    except Exception as e:
      print(e)
    finally:
        cursor.close()
        con.close()
        
if __name__ == "__main__":
    try:
      while True:
        selecao = input("1- cadastrar 2-buscar 3-editar 4-excluir 5-encerra: ")
        if selecao == "1":
            nome = input("informe a matricula")
            endereço = input("informe o nome")
            telefone = 1
            # note o uso da \ para escapar o caractere "
            #valores = "( \""+ matricula + "\", \"" + nome + "\", " + str(turma) + ")"
            valores = "( '{}', '{}', {})".format(nome, endereço, str(int(telefone)))
            query = "INSERT INTO  paciente (nome, endereço, telefone) VALUES" + valores+";"
            print(query)#Apenas para confirmar os valores enviados ao banco
            executar(query)

        elif selecao == "2":
            query = "SELECT * FROM {};".format(input("informe a tabela a ser consultada"))
            dados = buscar(query)
            for linha in dados:
                print(linha)

        elif selecao == "3":
            pass
        elif selecao == "4":
            nome = input("informe a nome: ")
            endereço = " '{}' ".format(endereço)
            query = "DELETE FROM paciente WHERE endereço =" + valores +";"
            print(query)#Apenas para confirmar os valores enviados ao banco
            executar(query)
        elif selecao == "5":
            break
            
    except Exception as e:
        print(str(e))