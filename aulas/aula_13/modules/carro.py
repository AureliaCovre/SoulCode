from modules.veiculo import Veiculo

class Carro(Veiculo):
    
    #vel_max = 0
    fabricante = ""
    motor = ""
    nome = "nome do carro"
        
    def print_vel_max(self):
        print ("velocidade do carro ", self.vel_max)
    
    def print_motor(self):
        print(self.motor)
        
    def print_nome(self):
        super().print_nome()
