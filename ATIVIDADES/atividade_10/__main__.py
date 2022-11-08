from modules.conector import interface

if __name__ == "__main__":
    try:
        interface_banco = interface("root", " ", "127.0.0.1", "departamentos")
        
        while True:
            print("1-Criar Trigger Update \n2-Criar Trigger Delete \n3-Inserir dados \n4-Deletar dados \n5-Selecionar tabela \n0-Sair")
            selecao = input("Digite uma opção: ")  
            
            #Criando a Trigger update
            if selecao == "1":
                dados1 = interface_banco.update()
            
             #Criando a Trigger delete   
            elif selecao == "2":        
                dados2 = interface_banco.apagar()
            
            # Função Insert
            elif selecao == "3":        
                venda = input("Digite o numero da venda: ")
                produto = input("Digite o código do produto: ")
                quantidade = input("Digite a quantidade: ")      
                dados3 = interface_banco.inserir(venda, produto, quantidade)
            
            # Função Delete
            elif selecao == "4":
                codvenda = input("Digite o código da venda: ")
                delete = interface_banco.deletar(codvenda)
            
            # Função Select
            elif selecao == "5":
                tabela = input("Digite o nome da tabela: ")
                select = interface_banco.selecionar("*", tabela, "")
                for row in select:
                    print(str(row))
                               
            elif selecao == "0":
                break
        
        
    except Exception as e:
        print("ERRO no main:", str(e))
        
        
