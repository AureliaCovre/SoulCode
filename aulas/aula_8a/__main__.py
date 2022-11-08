from modules.conector import interface_db
from modules.film import Film


if __name__ == "__main__":
    try:
        #Conexao com o banco, retorno de dados brutos
        interface_banco = interface_db("root", "aurelia1", "127.0.0.1", "sakila")
        dados_max = interface_banco.selecionar("film_id, title, release_year, length", "film", " length = (select MAX(length) from film)")
        dados_min = interface_banco.selecionar("film_id, title, release_year, length", "film", " length = (select MIN(length) from film)")

        #Organizacao dos dados brutos dentro de objetos
        lista_tamanho_max_film = []
        lista_tamanho_min_film = []
        for dado in dados_max:
            item = Film(dado[0],dado[1],dado[2], dado[3])
            lista_tamanho_max_film.append(item)
            title_film_max.index(item[3])
        for dado in dados_min:
            item = Film(dado[0],dado[1],dado[2], dado[3])
            lista_tamanho_min_film.append(item)

        #Utilizacao da lista de objetos, no caso procura-se o maior id dentro dos objetos
        title_film.index()
        print("o filme mais longo e o mais curto sao: ", )
        qtde_film = len(lista_film)
        # for i in range(len(lista_film)):
            # if lista_film[i].get_film_id() > qtde_id:
            #     maior_id = lista_film[i].get_film_id()
        print("ano com o maior numero de lançamentos foi: ", qtde_film)
                    
    except Exception as e:
        print(str(e))
