from modules.carro import Carro

class Ferrari(Carro):
    fabricante = "ferrari"
    nome = "nome da ferrari"
    
    def __init__(self):
        self.vel_max = 300
    
    def set_nome(self, nome):
        self.nome = nome
    
    def print_motor(self):
        print(" classe ferrari")
