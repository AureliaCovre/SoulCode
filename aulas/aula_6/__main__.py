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
      for row in cursor:
         print(str(row))
      cursor.close()
      con.close()
    except Exception as e:
      print(e)

if __name__ == "__main__":
    try:
        nome = "aurelia"
        endereço = "Rua 1"
        telefone = "3363-3333"
        # note o uso da \ para escapar o caractere "
        #valores = "( \""+ matricula + "\", \"" + nome + "\", " + str(turma) + ")"
        valores = "( \"{}\", \"{}\", {})".format(nome, endereço, telefone)
        query = "INSERT INTO paciente (nome, endereço, telefone) VALUES" + valores+";"
        print(query)#Apenas para confirmar os valores enviados ao banco
        executar(query)
        
        query = "SELECT * FROM paciente;"
        buscar(query)
    except Exception as e:
        print(str(e))
