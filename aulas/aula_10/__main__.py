from modules.connector import interface_db

if __name__ == "__main__":
    try:
      interface = interface_db("root", "aurelia1", "127.0.0.1", "departamentos") 
    
    #   inserirvenda = interface_bd.Inserir(2, "16", 6)
      
    #   funcaotrigger = interface_db.trigger_update(query)
       
      
    except Exception as e:
        print(str(e))
