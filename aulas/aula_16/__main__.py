# from modules.connector import conectar

# if __name__ == '__main__':
#     database = conectar()
#     collection_name = database['professores']
    

# item_details = collection_name.find()
# for item_c in item_details:
#     print(item_c)

from modules.connector import Interface_db
if __name__== "__main__":
    interface_mongo = Interface_db()
    print(interface_mongo.buscar())
