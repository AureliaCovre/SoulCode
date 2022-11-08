from modules.aluno import Aluno

class Aluno_m(Aluno):
    
    nota = ""
             
      
    def __init__(self, nome, rg, endereco, contato, matricula, nota):
        self.nota = nota
        super().__init__(nome, rg, endereco, contato, matricula)
            
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
    
    def set_nota(self, nota):
        self.nota = nota 
        
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
        
    def print_nota(self):
        print(self.nota)         
