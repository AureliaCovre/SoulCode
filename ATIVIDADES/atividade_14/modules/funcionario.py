from modules.pessoa import Pessoa

class Funcionario(Pessoa):
       
    id = ""
    cargo = ""
    
    def __init__(self, nome, rg, endereco, contato, id, cargo):
        self.id = id
        self.cargo = cargo
        super().__init__(nome, rg, endereco, contato) #no super coloca os dados da classe pai 
        
        """Construtor da classe Pessoa

        Args:
            nome (string): nome da classe Pessoa
            rg (int): rg da classe Pessoa
            endereco (string): endereco da classe Pessoa
            contato (int): telefone de contato da classe Pessoa
        """
         
    def set_nome(self, nome):
        self.nome = nome
    
    def set_rg(self, rg):
        self.rg = rg
        
    def set_endereco(self, endereco):
        self.endereco = endereco
        
    def set_contato(self, contato):
        self.contato = contato    
        
    def set_id(self, id):
        self.id = id 
    
    def set_cargo(self, cargo):
        self.cargo = cargo             
    
    def print_nome(self):
        print(self.nome)
    
    def print_rg(self):
        print(self.rg)        
      
    def print_endereco(self):
        print(self.endereco)
        
    def print_contato(self):
        print(self.contato)    
        
    def print_id(self):
        print(self.id)    
                  
    def print_cargo(self):
        print(self.cargo)    
                        
        