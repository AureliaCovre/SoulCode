try:
    alunos = ["maria","ricardo", "alice","manoel"]
    notas = []

    while notas !=0:
        item = input()
        if item == "":
            notas = 0
        else:
            alunos.append(item)

    print(alunos)
except Exception as e:
    print(str(e))
     
