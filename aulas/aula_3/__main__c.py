
def soma(x, y):
    """Retorna o resultado da soma de 2 valoes, x e y.

    Args:
        x (float): primeira parcela de soma
        y (float): primeira parcela de soma

    """
    try:
        print("O resultado da soma é: ", x+y)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    try:
        soma(5,8)
             
    except Exception as e:
        print(str(e))  
