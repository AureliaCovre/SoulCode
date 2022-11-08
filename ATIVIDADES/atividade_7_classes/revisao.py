#Crie uma classe em Python para modelar um objeto a sua escolha. 
#Deve conter pelo menos 5 atributos, construtor e getters e setters conforme necessário

class Cliente:
    numero_registro = []
    nome = ""
    cpf = 0
    endereco = ""
    telefone = 0
    
    # def __init__(self): #No construtor é sempre obrigatorio o self
        # """ Construtor da classe Cliente
        # Args:
        #     numero_registro (lista): Código único, identificador do cliente 
        #     nome (string): Nome do cliente
        #     cpf (inteiro): CPF do cliente
        #     endereco (string): Endereço do cliente
        #     telefone (inteiro): numero de telefone do cliente
        # """
        # try:
        #     #self.numero_registro = int(input("Insira o numero de registro do cliente:   "))
        #     self.nome = str(input("Insira o nome do cliente: "))
        #     self.cpf = int(input("Insira o numero do CPF:  "))
        #     self.endereco = str(input("Insira o endereço do cliente: "))
        #     self.telefone = int(input("Insira o numero do telefone: "))
        # except Exception as e:
        #     print(str(e))
        
    def __init__(self, nome, cpf, endereco, telefone):
       self.set_nome(nome)
       self.set_cpf(cpf)
       self.set_endereco(endereco)
       self.set_telefone(telefone)    
 
    def add_numero_registro(self, id):
        self.numero_registro.append(id)
    
    def set_nome(self, nome):
        self.nome = nome
           
    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_endereco(self, endereco):
        self.endereco = endereco
        
    def set_telefone(self, telefone):
        self.telefone = telefone  

    
    
    def get_nome(self):
        return self.nome      
                
    def get_cpf(self):
        return self.cpf   
    
    def get_endereco(self):
        return self.endereco  
    
    def get_telefone(self):
        return self.telefone  
    
       
               
            