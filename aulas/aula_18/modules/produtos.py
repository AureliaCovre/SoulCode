from modules.clientes import Clientes


class Produto(Clientes):
    
    

# FUNÇÃO PARA INSERIR DADOS    
    def inserir_dados1(self):
        produto = []
         
     
        for i in range(1):
            nome_produto = input('Nome produto : ')
            validade = input('Validade : ')
            valor = input('Valor : ')
            self.estoque = 50

            produto.append({ 'nome produto': nome_produto, 'validade':validade, 'Valor':valor , 'Quantidade estoque': self.estoque})
           



# APRESENTANDO OS DADOS DE PRODUTOS
           
        print('=-'*30)
        print('TODOS OS PRODUTOS')
        print('=-'*30)  
        
        for pessoa in produto:
            for chave, valor in pessoa.items():
                print("{} => {}".format(chave, valor))
                
    
    
    
    