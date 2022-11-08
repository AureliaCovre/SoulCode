# Tudo aqui não é orientado a objeto 

def servidor(servico, ip = "127.0.1.1", porta=""):
    print("O serviço  ", servico, "esta rodando em ", ip, ":", porta)

if __name__ == "__main__":
    servidor("banco de dados SQL", "127.0.0.1", "3306")

""" ------------------------------------------- """ 
# função de argumentos (* significa N argumentos)
def soma (*args): # * n sei a quantidade n args
    total = 0
    for i in args: # para cada item em args vou somar no total
        total += i
    print(total)
   
           
if __name__ == "__main__":
    soma(123,54,54,564564,5454,5454,5454,)
    
""" ------------------------------------------- """   
#função 
def soma (*valores): 
    total = 0
    for valor in valores: 
        total += valor
    return total
    
        
if __name__ == "__main__":
    print(soma(13,542,524,564564,5454,5454,5454,))

""" ------------------------------------------- """   
def media (*valores): 
    total = 0
    for valor in valores: 
        total += valor
    return total/len(valores)
    
        
if __name__ == "__main__":
    print(media(13,542,524,564564,5454,5454,5454,))
    
""" ------------------------------------------- """   
# ESSA FUNÇÃO É PARA QUANDO NÃO SEI QTAS CHAVES E VALORES VOU RECEBER
def conexao (**kwargs): # ** é chave e valor
    for chave, valor in kwargs.items():
        print(chave, valor)
        
if __name__ == "__main__":
    conexao(hostname="localhost", user="root", senha="123456")
    
""" ------------------------------------------- """      

