#classe c/ 5 atributos, const, gets e sets

class Test:
    # _id = 0 #evitar o uso de _var
    numero = 0
    nome = ""
    tel = ""
    cpf = ""
    id_compras = []
    
    def __init__(self, nome, cpf, numero, tel):
        #usandos os setters para fazer a funcao de "self.var = var"
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_numero(numero)
        self.set_tel(tel)
    
    def set_nome(self, nome):
        self.nome = nome
        
    def set_cpf(self, cpf):
        if Test.valida_cpf(cpf):
            self.cpf = cpf
        else:
            print("ERRO NO CPF!")
    
    def set_numero(self, numero):
        self.numero = numero

    def set_tel(self, tel):
        self.tel = tel
        
    def add_id_compra(self, id):
        self.id_compras.append(id)

    def get_nome(self):
        return self.nome
        
    def get_cpf(self):
        return self.cpf
    
    def get_numero(self):
        return self.numero

    def get_tel(self):
        return self.tel
        
    def get_id_compras(self):
        return self.id_compras

    def valida_cpf(cpf):
        if cpf is None:
            return 0
        else:
            return 1
