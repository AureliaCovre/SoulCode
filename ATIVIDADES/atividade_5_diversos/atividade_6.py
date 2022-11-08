#Crie um código que receba em sequencia de produtos contendo nome de produto, descrição, preço e quantidade em estoque.

try:
    cadastros = []
    while True:
        escolha1 = input("Cadastro de produtos: S/N ")
        escolha1 = escolha1.upper()
        if escolha1 =="S":
            cadastro = []
            cadastro.append(input("Insira o nome: "))
            cadastro.append(input("Insira a descrição: "))
            cadastro.append(input("Insira o preço: "))
            cadastro.append(input("Insira quantidade em estoque: "))
            cadastros.append(cadastro)
        elif escolha1 == "N":
            print("Cadastro finalizado")
            for cadastro in cadastros:
                print(cadastro)
            break
        else: 
            print("opção invalida")
                    
except Exception as e:
    print(str(e))