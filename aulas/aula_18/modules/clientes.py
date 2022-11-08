from modules.pessoas import Pessoa


class Clientes(Pessoa):
    
    
    def inserir_dados(self):
        
        clientes = []
        
        for i in range(1):
            id_cliente = input('Numero do cliente: ')
            contato = input('Contato email: ')
            
            
            clientes.append({ 'Numero do cliente': id_cliente, 'Contato email': contato})
        
        
        print('=-'*30)
        print('DADOS CLIENTES')
        print('=-'*30)  
        
        for pessoa in clientes:
            for chave, valor in pessoa.items():
                print("{} => {}".format(chave, valor))
        
        return super().inserir_dados()
