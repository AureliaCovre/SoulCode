try:
    idade = 60
    if idade < 18:
        print("Menor de idade")
    elif 18 <= idade < 60:
        print("Maior de Idade")
    elif 60 <= 120:
        print("Idoso")
    else:
        print("ERRO: valor: ", idade)

except Exception as e:
    print("ERRO: ", str(e))        
 