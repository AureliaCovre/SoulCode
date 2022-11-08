
class Funcionarios:
    nome_fun = ""
    indentifica = ""
    horas_trabalho = 0
    inicio_contrato = 0
    fim_contrato = 0
    quantidade_venda = 0
    
    
    def __init__(self,nome,indentifica):
        self.set_nome(nome)
        self.set_indentifica(indentifica)
    
    
    def set_nome(self, nome):
        self.nome_fun = nome
    
    def set_indentifica(self, indentifica):
        self.indentifica = indentifica
        
    def set_horas_trabalho(self, horas):
        self.horas_trabalho = horas
        
    def set_inicio_contrato(self, inicio):
        self.inicio_contrato = inicio
    

    def set_fim_contrato(self, fim):
        self.fim_contrato = fim
    
    def set_quantidade_venda(self, venda):
        self.quantidade_venda = venda
    
    
        
    def get_nome(self):
        return self.nome_fun
    
    def get_indentifica(self):
        return self.indentifica
    
    def get_horas_trabalho(self):
        return self.horas_trabalho
    
    def get_inicio_contrato(self):
        return self.inicio_contrato
    
    def get_fim_contrato(self):
        return self.fim_contrato
    
    def get_quantidade_venda(self):
        return self.quantidade_venda
    
    
    def to_dict(self):
        return {"nome_fun":self.get_nome(),"cpf":self.get_indentifica(),"horas_trabalho_mes":self.get_horas_trabalho(),"inicio_contrato": self.get_inicio_contrato(),"final_contrato":self.get_fim_contrato(),"total_venda":self.get_quantidade_venda()}
    
    
    