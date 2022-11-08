try:
    
    numero1 = int(input("Digite o numero 1: "))
    operacao = input("Digite a operação: ")
    numero2 = int(input("Digite o numero 2: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":    
        resultado = numero1 - numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    elif operacao == "*":        
        resultado = numero1 * numero2
    
    print(str(numero1 + " " + operacao + " " + numero2 + " = " + resultado))

except Exception as e:
    print("resultado")
    