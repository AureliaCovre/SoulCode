class alunos:
    matricula = ""
    nome = ""
    turma = 0

    def __init__(self, nome, matricula, turma):
      try:
        self.nome = nome
        self.matricula = matricula
        self.turma = turma
      except Exception as e:
          print(str(e))

    def apresentar(self):
        try:
            print("Aluno nome: ", self.nome," matricula: ", self.matricula, " estuda na turma: ", self.turma)
        except Exception as e:
          print(str(e))
