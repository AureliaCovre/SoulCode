#Crie um código que receba 2 números e resolva a potencia do primeiro ao segundo. Ex: 5², 3³, ...

try:
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite um numero: "))
    potencial = num1 ** num2

    print(potencial)
except Exception as e:
    print(str(e))  