from modules.pet import Pet

#Inicio do codigo, inicio do bloco principal
if __name__ == "__main__":
     #Instanciando a classe pet, criando o objeto pet_bob
    pet_bob = Pet("Bob", "doguinho", "medio")
    #Chamando um metodo da classe Pet, definindo o nome do proprietario
    pet_bob.set_proprietario_nome("Marcos")
    #Chamando um metodo da classe que retorna o nome do proprietario e apresenta na saida padrao
    print(pet_bob.get_proprietario_nome())
