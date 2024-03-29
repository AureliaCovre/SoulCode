from modules.conector import interface_banco

if __name__=="__main__":
    try:
        interfacedb = interface_banco("soulcode","senhasql","192.168.1.99","LOJA")

        while True:
        
            print("Escolha uma opção: \n")
            selecao =input(" \n1- select" 
                            "\n2- insert"
                            # "\n3- delete"
                            "\n3- total de vendas"
                            "\n4- Funcionário maior venda"
                            "\n5- Funcionario com maior quantidade"
                            "\n6- Fornecedor mais utilizado"
                            "\n7- Exibir o total de comissão"
                            "\n0- sair do sistema\n"
                            )
            
            if selecao=="1":
                dados=interfacedb.selecionar("*","venda","")
                print(dados)
            elif selecao=="2":
                #     id_produto INTEGER UNSIGNED NOT NULL,
                #     id_vendedor INTEGER UNSIGNED NOT NULL,
                #     valor_total DECIMAL(6,3) NOT NULL,
                #     comissao DECIMAL (6,2) NOT NULL,

                produto=input("Informe o id do produto: ")
                vendedor=input("Informe o id do vendedor: ")
                valor=float(input("Informe o valor da venda: "))
                comissao=str(0.08*valor)

                valores=produto+","+vendedor+","+str(valor)+","+comissao
                dados=interfacedb.inserir("venda","(id_produto, id_vendedor, valor_total, comissao)",valores)
            elif selecao=="3":
                soma_totalvendas = interfacedb.totalVendas()
                print(str(soma_totalvendas))
            elif selecao=="4": 
                print(interfacedb.maiorVenda())
            elif selecao=="5": 
                print(interfacedb.maiorQuantidadeDeVendas())
            elif selecao=="6":
                print(interfacedb.fornecedorMaisUtilizado())
            elif selecao=="7":
                print(interfacedb.comissao())
            elif selecao=="0":
                print("Sair do sistema")
                break
            else:
                print("Opção inválida. Favor digitar um número entre 0 e 4")
            input()
    except Exception as e:
        print(str(e))
