class Pessoa:
    nome = ""
    rg = ""
    endereco = ""
    contato = ""
    
    def __init__(self, nome, rg, endereco, contato):
        """Construtor da classe Pessoa

        Args:
            nome (string): nome da classe Pessoa
            rg (int): rg da classe Pessoa
            endereco (string): endereco da classe Pessoa
            contato (int): telefone de contato da classe Pessoa
        """
        try:
            self.nome = nome
            self.rg = rg
            self.endereco = endereco
            self.contato = contato
            
        except Exception as e:
            print(str(e))
          
    def print_nome(self):
        print(self.nome)
        
    def print_rg(self):
        print(self.rg)
        
    def print_endereco(self):
        print(self.endereco)    
        
    def print_contato(self):
        print(self.contato)     