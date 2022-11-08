import mysql.connector

class connector:
  user = ""
  password = ""
  host = ""
  db = ""

  def __init__(self, user, password, host, db):
      try:
          self.user = user
          self.password = password
          self.host = host
          self.db = db
      except Exception as e:
          print(str(e))

  def executar(self, query):#INSERT. UPDATE. DELETE
   try:
      con = mysql.connector.connect(user=self.user, password=self.password , host=self.host, database=self.db)
      cursor = con.cursor()
      cursor.execute(query)
      cursor.close()
      con.commit()
      con.close()
   except Exception as e:
    print(e)

  def buscar(self, query):#SELECT
    try:
      con = mysql.connector.connect(user=self.user, password=self.password , host=self.host, database=self.db)
      cursor = con.cursor()
      cursor.execute(query)
      return cursor.fetchall()
    except Exception as e:
      print(e)
    finally:
       cursor.close()
       con.close()
