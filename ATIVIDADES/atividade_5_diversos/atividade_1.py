#Crie um código que apresenta "Parabéns!" caso o usuário insira em sequência os números 1, 2, 3, e 4.

try:
    while True:
        num1  = input("Digite 1: ")
        num2  = input("Digite 2: ")
        num3  = input("Digite 3: ")
        num4  = input("Digite 4: ")
    
        if num1 == "1" and num2 == "2" and num3 == "3" and num4 == "4":
            print("Parabens!")
            break
        else:
            print("tente novamente") 

except Exception as e:
    print(str(e))
