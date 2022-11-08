try:
    nota_do_aluno = 72
    media_aprovacao = 60

    if nota_do_aluno >= media_aprovacao:
        print("Aprovado")

    else:
        print("reprovado")

except Exception as e:
    print(" erro no processo", str (e))  
