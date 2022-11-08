class cliente:
    nome = "teste"
    cpf = 0
    data_nascimento = 0

    def __init__(self, nome, cpf):          #self é o proprio objeto
        """ Construtor da classe cliente
        Args:
            nome (string): nome do cliente
            cpf(string): cpf do cliente
        """
        try:
            self.nome = nome
            self.cpf = str(cpf)
        except Exception as e:
            print(str(e))    

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome 

    def set_cpf(self, cpf):
        """Altera o cpf do cliente para valor informado
        Args:
        cpf (string): cpf do cliente
        """
        try:
            self.cpf = str(cpf)  
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    try:
        maria = cliente("maria", "2324232")
        print(maria.get_nome())
        
    except Exception as e:
        print(str(e))