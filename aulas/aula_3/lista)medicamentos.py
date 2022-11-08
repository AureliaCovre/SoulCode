class Medicamento:
    nome = "teste"
    fabricante = ""
    tipo = ""
    estoque = 0
    codigo = ""
    
    def __init__(self):
        """Construtor de medicamento.
        
        Args:
            nome (string): nome do medicamento
            fabricante (string): fabricante do medicamento
            tipo (string): original ou generico
            estoque (int): quantidade em estoque
            codigo (string): codigo do medicamento

        """
      
        try:
            self.nome = str(input("Nome do medicamento: "))
            self.fabricante = str(input("Fabricante"))
            self.tipo = str(input("Tipo do medicamento, original ou genérico: "))
            self.estoque = int(input("Estoque"))
            self.codigo = str(input("codigo"))

        except Exception as e:
            print (str(e))

    def set_nome (self,nome):
        self.nome = nome
    def set_fabricante (self,fabricante):
        self.fabricante = fabricante        
    def set_tipo (self,tipo):
        self.fabricante = tipo
    def set_estoque (self,estoque):
        self.estque = estoque    
    def set_codigo (self,codigo):
        self.codigo = codigo
    def print_atributos (self):
        print(f"{self.nome},{self.fabricante},{self.tipo},{self.estoque},{self.codigo}")


    def get_nome(self):
        return self.nome
    def get_fabricante(self):
        return self.fabricante
    def get_tipo(self):
        return self.tipo
    def get_estoque(self):
        return self.estoque
    def get_codigo(self):
        return self.codigo


if __name__== "__main__":

    Listamedicamento = []

    try:
        while True:
            opcao = input("Deseja digitar um novo medicamento? S/N - ")
            if opcao == "N" or opcao == "n" or opcao == "":
                break
            
            m = Medicamento()
            Listamedicamento.append(m)
        
        for medicamento in Listamedicamento:
            medicamento.print_atributos()
         
    except Exception as e:
        print (str(e))