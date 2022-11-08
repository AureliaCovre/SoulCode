import mysql.connector

class connector():
 def conectar():
   """Basic connection used to pass and receive data.
   """
   try:
      con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='clinica_boa_saude')
      query = "SHOW TABLES"
      cursor = con.cursor()
      cursor.execute(query)
      for row in cursor:
         print(str(row))
      cursor.close()
      con.close()
   except Exception as e:
    print(e)
