from modules.connector import Interface_db

if __name__ == "__main__":
   interface_mongo = Interface_db()
   # print(interface_mongo.buscar())
   # interface_mongo.inserir_um({"mateus":"TESTE", "idade":"34"})
   # print(interface_mongo.buscar())
   # interface_mongo.inserir_varios([{"nome":"testando", "idade":"40"},{"Ricardo":"testando", "idade":"40"}, {"natalia":"testando", "idade":"40"}])
   # print(interface_mongo.buscar())
   # interface_mongo.excluir_um({"mateus":"TESTE", "idade":"34"})
   # print(interface_mongo.buscar())
   interface_mongo.atualizar_um({"mateus":"LINDO", "idade":"34"})
   print(interface_mongo.buscar())
