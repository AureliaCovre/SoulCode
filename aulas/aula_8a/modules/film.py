
class Film:
    #atributos da classe
    idproduto = ""
    idvendedor = ""
    valor_total = ""
    comissao = ""
    
    def __init__(self, f_id, title, year, length):
        try:
            self.film_id = f_id
            self.title = title
            self.release_year = year
            self.length = length
        except Exception as e:
            print(str(e))
    
    def get_film_id(self):
        return self.film_id
    def get_title(self):
        return self.title
    def get_release_year(self):
        return self.release_year
    def get_length(self):
        return self.length