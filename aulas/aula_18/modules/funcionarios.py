from modules.pessoas import Pessoa

class Funcionarios(Pessoa):
    
    
    
    def inserir_dados(self):
        
        funcionarios = []
        
        for i in range(2):
            id = input('ID Funcionario : ')
            cargo = input('Cargo : ')
           
            
            funcionarios.append({ 'ID Funcionario': id, 'cargo': cargo})
           
        print('=-'*30)
        print('DADOS FUNCIONARIOS')
        print('=-'*30)  
        
        
        for pessoa in funcionarios:
            for chave, valor in pessoa.items():
                print("{} => {}".format(chave, valor))   
           
        print("----")   
        
        return super().inserir_dados()
    

        
     
    
