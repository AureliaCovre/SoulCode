from modules.veiculo import Veiculo
from modules.carro import Carro

#TODO: fix spelling mistakes
if __name__ == "__main__":
    bicicleta = Veiculo()
    bicicleta.vel_max = 32
    barco = Veiculo()
    barco.vel_max = 40
    
    fordT1 = Carro()
    fordT1.motor = "bem fraco"
    fordT1.vel_max = 50

    fordT1.print_vel_max()
    fordT1.print_motor()
