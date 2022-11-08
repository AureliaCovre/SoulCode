

class Pessoa: 
    pessoas = []
    
    
    
# CONSTRUTOR TRANSFORMANDO AS INFORMAÇÕES OBRIGATORIAS NO MAIN
    def __init__(self, pessoas):
        self.pessoas = pessoas
    
    
    
    def inserir_dados(self):
        
        self.pessoas = []
        
        for i in range(2):
            nome = input('Nome : ')
            cidade = input('Cidade : ')
            rg = input('RG : ')

            self.pessoas.append({ 'nome': nome, 'cidade':cidade, 'RG':rg })
        
        print("=_"*30) 
        
        for pessoa in self.pessoas:
            for chave, valor in pessoa.items():
                print("{} => {}".format(chave, valor))

        print("-"*30)
        