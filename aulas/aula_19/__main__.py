import pandas

dados = pandas.read_csv('DADOS_1.csv')
#.head() .tail()
"""Para iloc: [linha_comeco:linha_fim, coluna_comeco: coluna_fim] """
#.iloc[0]       -- obtém linhas (e / ou colunas) em localizações de inteiros.
# iloc[0:50]    -- localizou os 50 primeiros itens.
# iloc[:,2:3]
#.loc[:,'valor']]   -- obtém linhas (e / ou colunas) com rótulos específicos.
print(dados.iloc[:,2:3])
