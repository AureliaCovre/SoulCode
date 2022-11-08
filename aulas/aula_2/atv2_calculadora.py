try:
    primeiro = 7
    segundo = 5
    resultado = primeiro + segundo
    print("CALCULADORA_V0.01")
    print("o resultado da divisão é: ", primeiro / segundo)
    print("o resultado da soma é: ", resultado)
    print("o resultado da subtração é: ", primeiro - segundo)
    print("o resultado da multiplicação é: ", primeiro * segundo)

except Exception as erro:
    print("ERRO: ", str(erro))
    