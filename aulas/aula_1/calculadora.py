#Comentario é com a tralha
# o usuario não visualiza esses comentarios
#TODO: usualmente usado para marcar coisas a serem corrigidas ou adicionadas
""" Isto é um comentario para proposito de documentação. Veremos com mais detalhes na parte de função.
"""
try:
    primeiro = 5
    segundo = 0
    resultado = primeiro + segundo
    print("CALCULADORA_V0.01")
    print("o resultado da divisao é: ", primeiro / segundo)
    print("o resultado da soma é: ", resultado)
    print("o resultado da subtração é: ", primeiro - segundo)
    print("o resultado da multiplicação é: ", primeiro * segundo)
except Exception as erro:
    print("ERRO: ", str(erro))
print("o codigo não para")