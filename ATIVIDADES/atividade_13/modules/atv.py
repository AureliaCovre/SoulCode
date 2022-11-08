from modules.connector import Interface_db, get_db_info
import pandas as pd
import statistics as st

def chunk(dataframe):
    for i in range(0, len(dataframe), 50):
        yield dataframe[i:i + 50]
"""
    Definindo a função de para dividir os blocos em 50.   
"""        
     
def calculate_mean(list):
    return list[2].mean()
"""
    Definindo a função de calcular a mediana pela biblioteca pandas,
    ela passa pela lista no meu banco de dados e retorna o cálculo.      
"""
    
def calculate_median(list):
    return list[2].median()
"""
    Definindo a função de calcular a mediana pela biblioteca pandas,
    ela passa pela lista no meu banco de dados e retorna o cálculo.      
"""  
         
def calculate_mode(list):
    return list[2].mode
"""
    Definindo a função de calcular a moda pela biblioteca pandas,
    ela passa pela lista no meu banco de dados e retorna o cálculo.      
"""   
    
def calculate_standart_deviation(list):
    return list[2].std()  
"""
    Definindo a função de calcular a desvio padrão pela biblioteca statistics,
    ela passa pela lista no meu banco de dados e retorna o calculo      
"""
    
def calculate_maximum(list):
    return list[2].max 
"""
    Definindo a função de calcular o valor maximo utilizando a biblioteca pandas,
    ela passa pela lista no meu banco de dados e retorna o cálculo.      
""" 
    
def calculate_minimum(list):
    return list[2].min()
"""
    Definindo a função de calcular o valor minimo utilizando a biblioteca pandas,
    ela passa pela lista no meu banco de dados e retorna o cálculo.      
""" 
    
def calculate_date_maximum(list):
    list[1].astype('datetime64') 
    return list[1].max()
"""
    Definindo a função de localizar a maior data pela biblioteca statistics,
    ela passa pela lista no meu banco de dados e retorna com a data.    
"""
    
def calculate_date_minimum(list):
    list[1].astype('datetime64') 
    return list[1].min()

"""
    Definindo a função de localizar a menor data pela biblioteca statistics,
    ela passa pela lista no meu banco de dados e retorna com a data.    
"""

#funcao para buscar todos os itens da tabela 
def get_dados():
    try:
        query = f"SELECT id_operacao, data, valor FROM DADOS;"
        user, password, host, database = get_db_info()
        db = Interface_db(user, password, host, database)
        dados = db.selecionar(query)
        df = pd.DataFrame(dados)
        dados[2] = dados[2].astype('float')
        #sort pra ordenar os valores, by = numero da coluna
        df = df.sort_values(by = 1, ascending=True)
        chunked_df = chunk(df)
        for f_list in chunked_df:
            mean = calculate_mean(f_list)
            median = calculate_median(f_list)
            mode = calculate_mode(f_list)
            standart_deviation = calculate_standart_deviation(f_list)
            maximum = calculate_maximum(f_list)
            minimum = calculate_minimum(f_list)
            data_maximum = calculate_date_maximum(f_list)
            data_minimum = calculate_date_minimum(f_list)
            user, password, host, database = get_db_info()
            db = Interface_db(user,password, host, database)
            query = f"INSERT INTO media \
                (media, mediana, moda, desvio_padrao, maior, menor, data_inicio, data_fim) \
                VALUES \
                ('{mean}', '{median}', '{mode}', '{standart_deviation}', '{maximum}', '{minimum}', '{data_maximum}', '{data_minimum}');"
            db.executar(query)
            print("Insert realizado com sucesso")
    except Exception as e:
        print(str(e))  
            
            
# class Dados:
#     data_dados = ""
#     valor_dados = ""
    
#     #iniciando o construtor
#     def __init__(self, data_dados, valor_dados):
#         """Construtor da classe Dados

#         Args:
#             data_dados (date): data
#             valor_dados (numeric): valor
#         """
#         try:
#             self.data_dados = data_dados
#             self.valor_dados = valor_dados
#         except Exception as e:
#             print(str(e))
        
def calculo(dados):
        try:  
            df = pd.DataFrame(dados)
            print(df[2].mean())
            print(df[2].std())
            print(df[2].median())
            print(df[2].min())
            print(df[2].max())
            print(df[2].mode())
            print(len(df)/50)
            
            for i in range(int(len(df)/50)):
                slice 
        except Exception as e:
            print(str(e))
       
           
