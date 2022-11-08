#Crie um código em que o usuário digite o código de um estado e o computador apresente o estado por extenso. Ex: RJ > Rio de Janeiro

try:
    estados_brasileiros = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins", "Distrito Federal"]
    codigo_estadual = ["AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO", "DF"]

    while True:
        print("Digite a sigla desejada: ")
        estado = input()
        estado = estado.upper()
        for codigo in codigo_estadual:
            if estado == codigo:
                indice = codigo_estadual.index(estado)
                print(estados_brasileiros[indice])
                break
            
except Exception as e:
    print(str(e))
