#ESTRUTURA DE DECISAO 
try:
    total_de_vendas = 9875
    meta_de_vendas = 10000
    if total_de_vendas < meta_de_vendas:
        print("NAO ATINGIU A META! NÃOOOOOO")
    else:
        print("UHUL ATINGIMOS A META")

    if total_de_vendas >= meta_de_vendas:
        print("UHULL ATINGIMOS A META")
    else:
        print("NAO ATINGIMOS A META")

except Exception as e:
    print("ERRO: ", str(e))
                    
