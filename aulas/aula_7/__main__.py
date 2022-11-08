from modules.alunos import alunos
from modules.conector import conector

if __name__ == "__main__":
    try:
        con = conector("root", "admin", "127.0.0.1", "escola_123")
        query = "SELECT * FROM alunos"
        db_alunos = con.buscar(query)

        lista_alunos = []
        for al in db_alunos:
            aluno = alunos(al[1], al[0], al[2])
            lista_alunos.append(aluno)

        for aluno in lista_alunos:
            aluno.apresentar()
            
    except Exception as e:
        print(str(e))