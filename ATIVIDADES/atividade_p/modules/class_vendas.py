class Vendas:
    idprodutos = ""
    idvendedor = ""
    valor_total = ""
    comissao = ""
    
    def __init__(self, idprodutos, idvendedor, valor_total, comissao):
        try:
            self.idprodutos = idprodutos
            self.idvendedor = idvendedor
            self.valor_total = valor_total
            self.comissao = comissao
        except Exception as e:
            print(str(e))
    
    def get_idprodutos(self):
        return self.idprodutos
    def get_idvendedor(self):
        return self.idvendedor
    def get_valor_total(self):
        return self.valor_total
    def get_comissao(self):
        return self.comissao
