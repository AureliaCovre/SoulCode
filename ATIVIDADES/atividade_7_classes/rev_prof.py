
class Test:
    numero = 0
    nome = ""
    tel = ""
    cpf = ""
    id_compras = []
    
    #Aqui esta chamando a função
    def __init__(self, nome):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_numero(numero)
        self.set_tel(tel)
        
    #Aqui estou definindo a função    
    def set_nome(self, nome):
        self.nome = nome
        
    def set_cpf(self, cpf):
        if Test.valida_cpf(cpf):
            self.cpf = cpf
        else:
            print("ERRO NO CPF!")     
            
    def set_numero(self, numero):
        self.numero = numero
        
    def set_test(self, tel):
        self.tel = tel 
        
    #add pode substiruir o set nos casos de lista
    def add_id_compra(self, id):
        self.id_compras.append(id)                      