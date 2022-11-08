import mysql.connector

def executar(query):#INSERT. UPDATE. DELETE
   try:
      con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='escola_123')
      cursor = con.cursor()
      cursor.execute(query)
      cursor.close()
      con.commit()
      con.close()
   except Exception as e:
    print(e)

def buscar(query):#SELECT
    try:
      con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='escola_123')
      cursor = con.cursor()
      cursor.execute(query)
      for row in cursor:
         print(str(row))
      cursor.close()
      con.close()
    except Exception as e:
      print(e)

if __name__ == "__main__":
    try:
        matricula = "3934556"
        nome = "mauricio"
        turma = 1
        # note o uso da \ para escapar o caractere "
        #valores = "( \""+ matricula + "\", \"" + nome + "\", " + str(turma) + ")"
        valores = "( \"{}\", \"{}\", {})".format(matricula, nome, turma)
        query = "INSERT INTO alunos (matricula_aluno, nome_aluno, turma_aluno) VALUES" + valores+";"
        print(query)#Apenas para confirmar os valores enviados ao banco
        executar(query)
        query = "SELECT * FROM alunos;"
        buscar(query)
    except Exception as e:
        print(str(e))