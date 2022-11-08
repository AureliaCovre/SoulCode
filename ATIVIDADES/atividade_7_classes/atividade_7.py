#Crie uma classe em Python para modelar um objeto a sua escolha. 
#Deve conter pelo menos 5 atributos, construtor e getters e setters conforme necessário

class produto:
    produto = ""
    codigo = 0
    estoque = 0
    valor = 0
    cor = ""
                 
    def __init__(self):          
        """ Construtor da classe produto
        Args:
            produto (string): nome do produto
            codigo (inteiro): estoque de produtos
            estoque (inteiro): nome do produto
            valor (inteiro): valor do produto
            cor (string): cor do produto
        """
            
        try:
            self.produto = str(input("Nome do produto: "))
            self.codigo = int(input("Codigo do produto: "))
            self.estoque = int(input("Quantidade em estoque: "))
            self.valor = int(input("Valor de venda produto: "))
            self.cor = str(input("Cor do produto: "))
        except Exception as e:
            print(str(e))    

    def set_produto(self, produto):
        self.produto = produto
    def set_codigo(self, codigo):
        self.codigo = codigo
    def set_estoque(self, estoque):
        self.estoque = estoque 
    def set_valor(self, valor):
        self.valor = valor
    def set_cor(self, cor):
        self.cor = cor
    def print_atributos (self):
        print(f"{self.produto},{self.codigo},{self.estoque},{self.valor},{self.cor}")     
        
    def get_produto(self):
        return self.produto 
    def get_codigo(self):
        return self.codigo
    def get_estoque(self):
        return self.estoque 
    def get_valor(self):
        return self.valor
    def get_cor(self):
        return self.cor     

if __name__ == "__main__":
    
    Listaprodutos = []
     
    try:
        while True:
            opcao = input("Deseja iniciar o cadastro de produtos? S/N ")
            if opcao == "N" or opcao == "n" or opcao == " ":
                print("Cadastro finalizado!")
                break
                
            P = produto()
            Listaprodutos.append(P)
            
        for produto in Listaprodutos:
            produto.print_atributos()
    
    except Exception as e:
        print(str(e))
            
