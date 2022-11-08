#Definicao da classe, no caso chamada de Pet
class Pet:
    
    #Definicao dos atributos da classe
    pet_nome = ""
    proprietario_nome = ""
    proprietario_tel = ""
    pet_dt_nasc = ""
    pet_especie = ""
    pet_raca = ""
    pet_porte = ""
    observacao = ""

    #Definicao do construtor da classe, o construtor é opcional
    def __init__(self, nome, especie, porte):
        self.pet_nome = nome
        self.pet_especie = especie
        self.pet_porte = porte

    #Definicao dos metodos da classe
    #setter e getters sao funcoes set e get, usadas para alterar ou retornar os valores dos atributos
    def set_pet_nome(self, nome):
        self.pet_nome = nome
        
    def get_pet_nome(self):
        return self.pet_nome

    def set_proprietario_nome(self, nome):
        self.proprietario_nome = nome
        
    #Exemplo de um metodo com documentacao e tratamento de erro
    def get_proprietario_nome(self):
        """Retorna o nome do proprietario

        Returns:
            string: nome do proprietario
        """
        try:
            return self.proprietario_nome
        except Exception as e:
            print(str(e))
    
    # ... e assim por diante para os proximos atributos
    #TODO: get e set dos outros atributos
