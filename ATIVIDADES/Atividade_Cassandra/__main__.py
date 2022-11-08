#TODO:
# - crie uma classe com as funcoes basicas de interacao com um banco cassandra
# - implemente metodos para fetchall()
# - implemente exclusao e atualizacao de dados por chave que nao a primaria, ex: nome no caso do aluno


from modules.connector import ConexaoCassandra


if __name__ == "__main__":
    interfaceCassandra = ConexaoCassandra()
    # interface.inserir("uuid()", "marcia pereira", "rua marcia", "direito", "3333333")
    
    # interfaceCassandra.inserir("soulcode.alunos", "matricula, nome, endereco, curso, telefone", "uuid(), 'marcia', 'rua A', 'direito', '33333'")
    
    interfaceCassandra.select()
