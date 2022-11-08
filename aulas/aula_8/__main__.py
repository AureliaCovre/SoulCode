from modules.conector import interface_db
from modules.inventory import inventory

if __name__ == "__main__":
    try:
        #Conexao com o banco, retorno de dados brutos
        interface_banco = interface_db("root", "aurelia1", "127.0.0.1", "sakila")
        dados = interface_banco.selecionar("*", "inventory", "")

        #Organizacao dos dados brutos dentro de objetos
        lista_inventory = []
        for inv in dados:
            item = inventory(inv[0],inv[1],inv[2],inv[3])
            lista_inventory.append(item)

        #Utilizacao da lista de objetos, no caso procura-se o maior id dentro dos objetos
        maior_id = 0
        for i in range(len(lista_inventory)):
            if lista_inventory[i].get_inventory_id() > maior_id:
                maior_id = lista_inventory[i].get_inventory_id()
        print("maior id da tabela: ", maior_id)
                    
    except Exception as e:
        print(str(e))
