import mysql.connector

def executar(query):
   try:
      con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='mydb')
      cursor = con.cursor()
      cursor.execute(query)
      cursor.close()
      con.commit()
      con.close()
   except Exception as e:
    print(e)

def buscar(query):
    try:
      con = mysql.connector.connect(user='root', password='aurelia1', host='127.0.0.1', database='mydb')
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
        lista_cadastro = [(837, 981, 24.29, 1.94), (353, 684, 288.53, 23.08), (375, 362, 235.57, 18.85), (204, 270, 234.91, 18.79), (398, 577, 77.57, 6.21), (1828, 189, 257.52, 20.6), (250, 374, 229.13, 18.33), (591, 16, 3.45, 0.28), (1270, 978, 262.74, 21.02), (1625, 861, 41.92, 3.35), (1876, 250, 209.17, 16.73), (1554, 421, 121.04, 9.68), (1542, 507, 210.53, 16.84), (531, 300, 44.87, 3.59), (595, 739, 44.45, 3.56), (1027, 528, 98.67, 7.89), (815, 521, 59.05, 4.72), (99, 294, 286.39, 22.91), (247, 121, 56.18, 4.49), (1286, 757, 244.95, 19.6), (1659, 395, 211.06, 16.88), (906, 895, 260.85, 20.87), (490, 976, 82.23, 6.58), (359, 239, 160.61, 12.85), (1322, 863, 118.79, 9.5), (294, 474, 213.15, 17.05), (711, 742, 257.17, 20.57), (1320, 245, 243.62, 19.49), (316, 385, 212.21, 16.98), (1216, 726, 199.32, 15.95), (1929, 178, 27.63, 2.21), (1690, 632, 174.55, 13.96), (1207, 957, 213.06, 17.04), (865, 55, 151.96, 12.16), (1717, 281, 174.08, 13.93), (339, 519, 285.78, 22.86), (1122, 499, 80.4, 6.43), (1970, 450, 186.29, 14.9), (791, 124, 21.99, 1.76), (725, 207, 80.41, 6.43), (1330, 804, 23.91, 1.91), (537, 825, 181.8, 14.54), (1909, 259, 141.55, 11.32), (1799, 982, 87.8, 7.02), (1544, 400, 38.66, 3.09), (1697, 670, 274.19, 21.94), (1966, 696, 181.78, 14.54), (1286, 866, 289.62, 23.17), (470, 306, 176.77, 14.14), (540, 25, 57.29, 4.58)]
        
        for vendas in lista_cadastro:
            valores = "({}, {}, {}, {})".format(*vendas)
            query = "INSERT INTO vendas(idproduto, idvendedor, valor_total, comissão) VALUES" + valores+";"
            print(query)
            executar(query)
       
    except Exception as e:
        print(str(e))  