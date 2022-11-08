class cliente:
    nome = "teste"
    cpf = 0
    data_nascimento = 0

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
        maria = cliente()
        joao = cliente()
        maria.set_nome("maria")
        joao.set_nome("joao")
        print(maria.get_nome())
        
    except Exception as e:
        print(str(e))