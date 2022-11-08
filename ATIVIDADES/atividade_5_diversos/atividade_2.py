#Crie um código que pede nomes em sequencia, e apresenta a lista completa conforme o usuário digita.

try:
    lista = []

    while True:
        print("cadastro")  
        opcao = input("Insira um nome: ")
      
        if opcao == "":
            break
        lista.append(opcao)
        print(lista)        

except Exception as e:
    print(str(e))