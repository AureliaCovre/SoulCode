def soma(x, y):
    """ Retorna o resultado da soma de 2 valores, x e y.
    Args:
    x (float): primeira parcela da soma
    y (float):  primeira parcela da soma
    """
    try:
        while True:
            x = float(x)
            y = float(y)
            print("O resultado da soma é: ", x+y)
            break
    except Exception as e:
        print(str(e))    

def subtracao(x,y):
    """ Retorna o resultado da subtração de 2 valores, x e y.
    Args:
    x (float): primeira parcela da subtracao
    y (float):  primeira parcela da subtracao
    """       
    try:
        while True:
            x = float(x)
            y = float(y)
            print("o resultado da subtração é: ", x-y)
            break
    except Exception as e:
        print(str(e))

def multiplicacao (x,y):
    """ Retorna o resultado da multiplição de 2 valores, x e y.
    Args:
    x (float): primeira parcela da multiplicação
    y (float):  primeira parcela da multiplicação
    """
    try:
        while True:
            x = float(x)
            y = float(y)
            print("o resultado da multiplicação é: ", x*y)
            break
    except Exception as e:
        print(str(e))


def divisao (x,y):
    """ Retorna o resultado da divisão de 2 valores, x e y.
    Args:
    x (float): primeira parcela da divisão
    y (float):  primeira parcela da divisão
    """
    try:
        while True:
            x = float(x)
            y = float(y)
            print("o resultado da divisão é: ", x/y)
            break
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    try:
        x = float(input("Digite o valor de x: "))
        y = float(input("Digite o valor de y: "))  

        soma(x,y)
        subtracao(x,y)
        divisao(x,y)
        multiplicacao(x,y)
    except Exception as e:
        print(str(e))