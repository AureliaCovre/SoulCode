#aqui ele mostra o resultados das somas que deram certo 
try:
    print("CALCULADORA_V0.01")
    primeiro =5
    segundo = 0
    resultado = primeiro + segundo
except Exception as erro:
    print("ERRO: ", str(erro))
    
try: 
    print("o resultado da divisão é: ", primeiro / segundo)
except Exception as erro:
    print("ERRO: ", str(erro))
   
try: 
    print("o resultado da soma é: ", resultado)
except Exception as erro:
    print("ERRO: ", str(erro))
    
try:
    print("o resultado da subtração é: ", primeiro - segundo)
except Exception as erro:
    print("ERRO: ", str(erro))
    
try:
    print("o resultado da multiplicação é: ", primeiro * segundo)
except Exception as erro:
    print("ERRO: ", str(erro))
    
finally:
    print("o codigo nao para")
