class Item:
    
    nome = ""
    cpf = ""
    
    
    #Construtor init - Não cria o objeto se não tiver todos os atibutos, ou seja torna os atributos obrigatorios!
    """ Exemplo no cadastro de uma loja , nome, cpf e endereço são obrigatorios mas e-mail é opcional"""
        
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def get_nome (self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def set_nome(self, nome):
        self.nome = nome
        
    def set_cpf(self, cpf):
        self.cpf = cpf   
     
    # Função de dicionario    
    def trazer_dicionario (self):
        return {"nome": self.get_nome(), "cpf": self.get_cpf()}
