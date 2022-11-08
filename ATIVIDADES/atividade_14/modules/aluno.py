from modules.pessoa import Pessoa

class Aluno(Pessoa):
        
    matricula = ""
    
    def __init__(self, nome, rg, endereco, contato, matricula):
        self.matricula = matricula
        super().__init__(nome, rg, endereco, contato) #no super coloca os dados da classe pai 
         
    def set_nome(self, nome):
        self.nome = nome
    
    def set_rg(self, rg):
        self.rg = rg
        
    def set_endereco(self, endereco):
        self.endereco = endereco
        
    def set_contato(self, contato):
        self.contato = contato  
    
    def set_matricula(self, matricula):
        self.matricula = matricula              
    
    def print_nome(self):
        print(self.nome)
    
    def print_rg(self):
        print(self.rg)        
      
    def print_endereco(self):
        print(self.endereco)
        
    def print_contato(self):
        print(self.contato) 
        
    def print_matricula(self):
        print(self.matricula)        