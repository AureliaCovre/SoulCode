from modules.connector import connector

if __name__ == "__main__":
    
    try:
        
        connector.conectar()
        
    except Exception as e:
        print(str(e))
