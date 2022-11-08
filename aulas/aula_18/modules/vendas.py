from modules.produtos import Produto
from modules.clientes import Clientes

class Vendas(Produto):
    
    vendas = []
    
    
    def inserir_dados1(self):
        return super().inserir_dados1() 
    
# FUNÇÃO CHAMANDO OS DADOS DE PRODUTOS E CLIENTES PARA RETORNAR    
    def inserir_dados(self):
    
        vendas = []
        
        for i in range(1):
            id_venda = input('ID Vendas : ')
            quantidade = int(input('Quantidade comprada: '))
               

            vendas.append({ 'ID Vendas': id_venda, 'Quantidade comprada': quantidade })
        
        print('=-'*30)
        print('AS VENDAS FEITAS')
        print('=-'*30)  
        
        
        while True:
                x = quantidade
                self.estoque = 50
                total = []
                if x <= self.estoque:
                    total =  self.estoque - x
                else:
                    break
                
                break

# PRINTANDO AS INFORMAÇÕES DE VENDAS  
            
        print("O que sobrou no estoque foi: ", total)
        for pessoa in vendas:
            for chave, valor in pessoa.items():
                
                print("{} => {}".format(chave, valor))
        print("=_"*30) 
            
           
        return super().inserir_dados()
        

    