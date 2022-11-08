# Equipe: Aurélia, Joyce e Ricardo

""" Atividade 17 - Spark inicial
Fonte: https://www.portaltransparencia.gov.br/download-de-dados/servidores
DATA FRAME ESCOLHIDA: APOSENTADOS_BACEN 
PERIODO: JAN e FEV DE 2021

Obs.: A intenção inicial era ser feita no primeiro trimestre de 2021, porém pelo fato dos
arquivos serem muito grandes não rodou em alguns computadores da equipe e por isso,
foi conversado com prof. Adriano e ele orientou/autorizou a fazer com apenas 2.
"""
# ----------------------------------------------------------
from os import replace, scandir, truncate
from typing import Collection
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as B
from pyspark.sql.types import FloatType 
from functools import reduce
from pyspark.sql import DataFrame
from pyspark.sql.functions import col , column, instr
import pandas as pd
from pyspark.sql import Row, context
import numpy as np

                
spark = SparkSession.builder.appName("OTR").config("spark.sql.caseSensitive", "True").getOrCreate()
dados1 = spark.read.format("csv").option("header", "true").option("delimiter",";").option("inferSchema", "true").option("encoding", "ISO-8859-1").load(r"C:\Users\Cleberson\Desktop\ATIVIDADE 17\202101_Pensionistas_DEFESA\202101_Remuneracao.csv")
dados2 = spark.read.format("csv").option("header", "true").option("delimiter",";").option("inferSchema", "true").option("encoding", "ISO-8859-1").load(r"C:\Users\Cleberson\Desktop\ATIVIDADE 17\202102_Pensionistas_DEFESA\202102_Remuneracao.csv")

print(50 * '=')
dadosunidos1 = dados1.union(dados2)


df = 0
ano = ''
mes = 0 
id_servidor_portal = 0
cpf = ''
nome = ''
remuneracao_basica_bruta_real = ''
remuneracao_basica_bruta_dolar  = ''
abate_teto_real = ''
abate_teto_dolar = ''
gratificacao_natalina_real = ''
gratificacao_natalina_dolar = ''
abate_teto_gratificacao_natalina_real = ''
abate_teto_gratificacao_natalina_dolar = ''
ferias_real = '' 
ferias_dolar = ''
outras_remuneracoes_eventuais_real = ''
outras_remuneracoes_eventuais_dolar = ''
irrf_real = ''
irrf_dolar = ''
pss_rpgs_real = ''
pss_rpgs_dolar = ''
demais_deducoes_real = ''
demais_deducoes_dolar = ''
pensao_militar_real  = ''
pensao_militar_dolar = ''
fundo_saude_real = ''
fundo_saude_dolar = ''
taxa_ocupacao_imovel_funcional_real = ''
taxa_ocupacao_imovel_funcional_dolar = ''
remuneracao_deducoes_obrigatorias_real = ''
remuneracao_deducoes_obrigatorias_dolar = ''
verbas_indenizatorias_registradas_sistemas_pessoal_civil_real = ''
verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar = ''
verbas_indenizatorias_registradas_sistemas_pessoal_militar_real = ''
verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar = ''
verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real = ''
verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar = ''
total_verbas_indenizatorias_real = ''
total_verbas_indenizatorias_dolar = ''


# VARIAVEIS QUE SOMAM OS NULOS EM CADA COLUNA
nulos0 = 0
nulos1 = 0
nulos2 = 0
nulos3 = 0
nulos4 = 0
nulos5 = 0
nulos6 = 0
nulos7 = 0
nulos8= 0
nulos9 = 0
nulos10 = 0
nulos11 = 0
nulos12 = 0
nulos13 = 0
nulos14 = 0
nulos15 = 0
nulos16 = 0
nulos17 = 0
nulos18 = 0
nulos19 = 0
nulos20 = 0
nulos21 = 0
nulos22 = 0
nulos23 = 0
nulos24 = 0
nulos25 = 0
nulos26 = 0
nulos27 = 0
nulos28 = 0
nulos29 = 0
nulos30 = 0
nulos31 = 0
nulos32 = 0
nulos33 = 0
nulos34 = 0
nulos35 = 0
nulos36 = 0
nulos37 = 0 
nulos38 = 0

listao_nulos = []


for alfa in range(1):
    usuario = input('Deseja normalizar os CSVs [s/n]? ')
   
    if usuario == 's':
        
        # 0
        lista0 = []
      
        for a in dadosunidos1.collect():
            ano = a[0]  #Iterando pelo numero pela coluna 
            ano = str(ano).replace(',', '.') #Convertendo a virgula em ponto
            
            if ano == 'None':
                nulos0 += 1 #contando a qtd de nulos
                listao_nulos.append(nulos0)
            
            ano = str(ano).replace('None', 'vazio') #Substituindo os campos com none por vazio
            lista0.append(ano)
       
        lista0 = lista0
        print('Ano')
        print('Ano máximo: ',max(lista0))     # Averiguando para saber se a coluna contem informações uteis
        print('Ano mínimo: ',min(lista0))     # Averiguando para saber se a coluna contem informações uteis
        print('Quantidade de nulos:', nulos0) # Averiguando se sobrou algum nulo
        print()

        # 1
        lista1 = []
    
        for b in dadosunidos1.collect():
            mes = b[1]
            mes = str(mes).replace(',', '.')
            
            if mes == 'None':
                nulos1 += 1 
                listao_nulos.append(nulos1)
            
            mes = str(mes).replace('None', 'vazio')
            lista1.append(mes)
    
        lista1 = lista1 
        print('Mês')
        print('Mês máximo: ',max(lista1))
        print('Mês mínimo: ',min(lista1))
        print('Quantidade de nulos:', nulos1)
        print()

        # 2
        lista2 = []
       
        for c in dadosunidos1.collect():
            id_servidor_portal = c[2]
            id_servidor_portal = str(id_servidor_portal).replace(',', '.')
            
            if id_servidor_portal == 'None':
                nulos2 += 1
                listao_nulos.append(nulos2)
            
            id_servidor_portal = str(id_servidor_portal).replace('None', '0')
            id_servidor_portal = int(id_servidor_portal)
            lista2.append(id_servidor_portal)
        
        lista2 = lista2 
        print('Id_servidor_portal')
        print('Valor máximo: ',max(lista2))
        print('Valor mínimo: ',min(lista2))
        print('Quantidade de nulos:', nulos2)
        print()

        # 3
        lista3 = []
      
        for d in dadosunidos1.collect():
            cpf = d[3]
            cpf = str(cpf).replace(',', '.')
            
            if cpf == 'None':
                nulos3 += 1
                listao_nulos.append(nulos3)
            
            cpf = str(cpf).replace('None', 'vazio')
            lista3.append(cpf)
           
        lista3 = lista3
        print('Cpf')
        print('Valor máximo: ',max(lista3))
        print('Valor mínimo: ',min(lista3))
        print('Quantidade de nulos:', nulos3)
        print()

        # 4
        lista4 = []
        nulos4 = 0
     
        for e in dadosunidos1.collect():
            nome = e[4]
            nome = str(nome).replace(',', '.')
            
            if nome  == 'None':
                nulos4 += 1
                listao_nulos.append(nulos4)
            
            nome  = str(nome ).replace('None', 'vazio')
            lista4.append(nome )

        lista4 = lista4
        print('Nome')
        print('Quantidade de nulos:', nulos4)
        print()

        # 5
        lista5 = []
    
        for f in dadosunidos1.collect():
            remuneracao_basica_bruta_real = f[5]
            remuneracao_basica_bruta_real = str(remuneracao_basica_bruta_real).replace(',', '.')
            
            if remuneracao_basica_bruta_real   == 'None':
                nulos5 += 1
                listao_nulos.append(nulos5)
            
            remuneracao_basica_bruta_real = str(remuneracao_basica_bruta_real).replace('None', '0.0')
            remuneracao_basica_bruta_real = float(remuneracao_basica_bruta_real)
            lista5.append(remuneracao_basica_bruta_real)

        lista5 = lista5 
        print('Remuneracao_basica_bruta_real')
        print('Valor máximo: ',max(lista5))
        print('Valor mínimo: ',min(lista5))
        print('Quantidade de nulos:', nulos5)
        print()

        # 6 
        lista6 = []
          
        for g in dadosunidos1.collect():
            remuneracao_basica_bruta_dolar  = g[6]
            remuneracao_basica_bruta_dolar  = str(remuneracao_basica_bruta_dolar).replace(',', '.')
            
            if remuneracao_basica_bruta_dolar   == 'None':
                nulos6 += 1
                listao_nulos.append(nulos6)
            
            remuneracao_basica_bruta_dolar   = str(remuneracao_basica_bruta_dolar  ).replace('None', '0.0')
            remuneracao_basica_bruta_dolar = float(remuneracao_basica_bruta_dolar)
            lista6.append(remuneracao_basica_bruta_dolar)
            
        lista6 = lista6
        print('Remuneracao_basica_bruta_dolar')
        print('Valor máximo: ',max(lista6))
        print('Valor mínimo: ',min(lista6))
        print('Quantidade de nulos:', nulos6)
        print()

        # 7
        lista7 = []
    
        for h in dadosunidos1.collect():
            abate_teto_real  = h[7]
            abate_teto_real  = str(abate_teto_real).replace(',', '.')
            
            if abate_teto_real   == 'None':
                nulos7 += 1
                listao_nulos.append(nulos7)
            
            abate_teto_real = str(abate_teto_real ).replace('None', '0.0')
            abate_teto_real = float(abate_teto_real)
            lista7.append(abate_teto_real)

        lista7 = lista7
        print('Abate_teto_real')
        print('Valor máximo: ',max(lista7))
        print('Valor mínimo: ',min(lista7))
        print('Quantidade de nulos:', nulos7)
        print()


        # 8
        lista8 = []
            
        for i in dadosunidos1.collect():
            abate_teto_dolar = i[8]
            abate_teto_dolar = str(abate_teto_dolar).replace(',', '.')
            
            if abate_teto_dolar   == 'None':
                nulos8 += 1
                listao_nulos.append(nulos8)
            
            abate_teto_dolar = str(abate_teto_dolar).replace('None', '0.0')
            abate_teto_dolar = float(abate_teto_dolar)
            lista8.append(abate_teto_dolar  )

        lista8 = lista8
        print('Abate_teto_dolar')
        print('Valor máximo: ',max(lista8))
        print('Valor mínimo: ',min(lista8))
        print('Quantidade de nulos:', nulos8)
        print()

        # 9
        lista9 = []
         
        for j in dadosunidos1.collect():
            gratificacao_natalina_real  = j[9]
            gratificacao_natalina_real  = str(gratificacao_natalina_real).replace(',', '.')
            
            if gratificacao_natalina_real == 'None':
                nulos9 += 1
                listao_nulos.append(nulos9)
            
            gratificacao_natalina_real = str(gratificacao_natalina_real).replace('None', '0.0')
            gratificacao_natalina_real = float(gratificacao_natalina_real)
            lista9.append(gratificacao_natalina_real)

        lista9 = lista9
        print('Gratificacao_natalina_real')
        print('Valor máximo: ',max(lista9))
        print('Valor mínimo: ',min(lista9))
        print('Quantidade de nulos:', nulos9)
        print()

        # 10
        lista10 = []
      
        for k in dadosunidos1.collect():
            gratificacao_natalina_dolar  = k[10]
            gratificacao_natalina_dolar  = str(gratificacao_natalina_dolar).replace(',', '.')
            
            if gratificacao_natalina_dolar == 'None':
                nulos10 += 1
                listao_nulos.append(nulos10)
            
            gratificacao_natalina_dolar = str(gratificacao_natalina_dolar).replace('None', '0.0')
            gratificacao_natalina_dolar = float(gratificacao_natalina_dolar)
            lista10.append(gratificacao_natalina_dolar)
            
        lista10 = lista10    
        print('Gratificacao_natalina_dolar')
        print('Valor máximo: ',max(lista10))
        print('Valor mínimo: ',min(lista10))
        print('Quantidade de nulos:', nulos10)
        print()

        # 11
        lista11 = []  
     
        for m in dadosunidos1.collect():
            abate_teto_gratificacao_natalina_real  = m[11]
            abate_teto_gratificacao_natalina_real  = str(abate_teto_gratificacao_natalina_real).replace(',', '.')
            
            if abate_teto_gratificacao_natalina_real == 'None':
                nulos11 += 1
                listao_nulos.append(nulos11)
            
            abate_teto_gratificacao_natalina_real = str(abate_teto_gratificacao_natalina_real).replace('None', '0.0')
            abate_teto_gratificacao_natalina_real = float(abate_teto_gratificacao_natalina_real)
            lista11.append(abate_teto_gratificacao_natalina_real)
            
        lista11 = lista11
        print('Abate_teto_gratificacao_natalina_real')
        print('Valor máximo: ',max(lista11))
        print('Valor mínimo: ',min(lista11))
        print('Quantidade de nulos:', nulos11)
        print()

        # 12
        lista12 = []
             
        for n in dadosunidos1.collect():
            abate_teto_gratificacao_natalina_dolar  = n[12]
            abate_teto_gratificacao_natalina_dolar  = str(abate_teto_gratificacao_natalina_dolar).replace(',', '.')
            
            if abate_teto_gratificacao_natalina_dolar == 'None':
                nulos12 += 1
                listao_nulos.append(nulos12)
            
            abate_teto_gratificacao_natalina_dolar = str(abate_teto_gratificacao_natalina_dolar).replace('None', '0.0')
            abate_teto_gratificacao_natalina_dolar = float(abate_teto_gratificacao_natalina_dolar)
            lista12.append(abate_teto_gratificacao_natalina_dolar)

        lista12 = lista12  
        print('Abate_teto_gratificacao_natalina_dolar')
        print('Valor máximo: ',max(lista12))
        print('Valor mínimo: ',min(lista12))
        print('Quantidade de nulos:', nulos12)
        print()

        # 13
        lista13 = []
           
        for o in dadosunidos1.collect():
            ferias_real  = o[13]
            ferias_real  = str(ferias_real).replace(',', '.')
            
            if ferias_real == 'None':
                nulos13 += 1
                listao_nulos.append(nulos13)
            
            ferias_real = str(ferias_real).replace('None', '0.0')
            ferias_real = float(ferias_real)
            lista13.append(ferias_real)

        lista13 = lista13
        print('Ferias_real')
        print('Valor máximo: ',max(lista13))
        print('Valor mínimo: ',min(lista13))
        print('Quantidade de nulos:', nulos13)
        print()

        # 14
        lista14 = []       
        
        for p in dadosunidos1.collect():
            ferias_dolar  = p[14]
            ferias_dolar  = str(ferias_dolar).replace(',', '.')
            
            if ferias_dolar == 'None':
                nulos14 += 1
                listao_nulos.append(nulos14)
            
            ferias_dolar = str(ferias_dolar).replace('None', '0.0')
            ferias_dolar = float(ferias_dolar)
            lista14.append(ferias_dolar)
            
        lista14 = lista14 
        print('Ferias_dolar')
        print('Valor máximo: ',max(lista14))
        print('Valor mínimo: ',min(lista14))
        print('Quantidade de nulos:', nulos14)
        print()

        # 15
        lista15 = []     
    
        for q in dadosunidos1.collect():
            outras_remuneracoes_eventuais_real  = q[15]
            outras_remuneracoes_eventuais_real  = str(outras_remuneracoes_eventuais_real).replace(',', '.')
            
            if outras_remuneracoes_eventuais_real == 'None':
                nulos15 += 1
                listao_nulos.append(nulos15)
            
            outras_remuneracoes_eventuais_real = str(outras_remuneracoes_eventuais_real).replace('None', '0.0')
            outras_remuneracoes_eventuais_real = float(outras_remuneracoes_eventuais_real)
            lista15.append(outras_remuneracoes_eventuais_real)

        lista15 = lista15
        print('Outras_remuneracoes_eventuais_real')
        print('Valor máximo: ',max(lista15))
        print('Valor mínimo: ',min(lista15))
        print('Quantidade de nulos:', nulos15)
        print()
            
        # 16
        lista16 = []
            
        for r in dadosunidos1.collect():
            outras_remuneracoes_eventuais_dolar  = r[16]
            outras_remuneracoes_eventuais_dolar  = str(outras_remuneracoes_eventuais_dolar).replace(',', '.')
            
            if outras_remuneracoes_eventuais_dolar == 'None':
                nulos16 += 1
                listao_nulos.append(nulos16)
            
            outras_remuneracoes_eventuais_dolar = str(outras_remuneracoes_eventuais_dolar).replace('None', '0.0')
            
            outras_remuneracoes_eventuais_dolar = float(outras_remuneracoes_eventuais_dolar)
            lista16.append(outras_remuneracoes_eventuais_dolar)

        lista16 = lista16
        print('outras_remuneracoes_eventuais_dolar')
        print('Valor máximo: ',max(lista16))
        print('Valor mínimo: ',min(lista16))
        print('Quantidade de nulos:', nulos16)
        print()

        # 17
        lista17 = []       
      
        for s in dadosunidos1.collect():
            irrf_real  = s[17]
            irrf_real  = str(irrf_real).replace(',', '.')
            
            if irrf_real == 'None':
                nulos17 += 1
                listao_nulos.append(nulos17)
            
            irrf_real = str(irrf_real).replace('None', '0.0')
            irrf_real = float(irrf_real)
            lista17.append(irrf_real)

        lista17 = lista17
        print('Irrf_real')
        print('Valor máximo: ',max(lista17))
        print('Valor mínimo: ',min(lista17))
        print('Quantidade de nulos:', nulos17)
        print()

        # 18
        lista18 = []     

        for t in dadosunidos1.collect():
            irrf_dolar = t[18]
            irrf_dolar = str(irrf_dolar).replace(',', '.')
            
            if irrf_dolar == 'None':
                nulos18 += 1
                listao_nulos.append(nulos18)
            
            irrf_dolar = str(irrf_dolar).replace('None', '0.0')
            irrf_dolar = float(irrf_dolar)
            lista18.append(irrf_dolar)
        
        lista18 = lista18
        print('Irrf_dolar')
        print('Valor máximo: ',max(lista18))
        print('Valor mínimo: ',min(lista18))
        print('Quantidade de nulos:', nulos18)
        print()

        # 19
        lista19 = []
       
        for u in dadosunidos1.collect():
            pss_rpgs_real = u[19]
            pss_rpgs_real = str(pss_rpgs_real).replace(',', '.')
            
            if pss_rpgs_real == 'None':
                nulos19 += 1
                listao_nulos.append(nulos19)
            
            pss_rpgs_real = str(pss_rpgs_real).replace('None', '0.0')
            pss_rpgs_real = float(pss_rpgs_real)
            lista19.append(pss_rpgs_real)
        
        lista19 = lista19 
        print('Pss_rpgs_real')
        print('Valor máximo: ',max(lista19))
        print('Valor mínimo: ',min(lista19))
        print('Quantidade de nulos:', nulos19)
        print()

        # 20
        lista20 = []
      
        for v in dadosunidos1.collect():
            pss_rpgs_dolar = v[20]
            pss_rpgs_dolar = str(pss_rpgs_dolar).replace(',', '.')
            
            if pss_rpgs_dolar == 'None':
                nulos2 += 1
                listao_nulos.append(nulos20)
            
            pss_rpgs_dolar = str(pss_rpgs_dolar).replace('None', '0.0')
            pss_rpgs_dolar = float(pss_rpgs_dolar)
            lista20.append(pss_rpgs_dolar)
        
        lista20 = lista20 
        print('pss_rpgs_dolar')
        print('Valor máximo: ',max(lista20))
        print('Valor mínimo: ',min(lista20))
        print('Quantidade de nulos:', nulos20)
        print()

        # 21
        lista21 = []
        nulos21 = 0
     
        for x in dadosunidos1.collect():
            demais_deducoes_real = x[21]
            demais_deducoes_real = str(demais_deducoes_real).replace(',', '.')
            
            if demais_deducoes_real == 'None':
                nulos21 += 1
                listao_nulos.append(nulos21)
            
            demais_deducoes_real = str(demais_deducoes_real).replace('None', '0.0')
            demais_deducoes_real = float(demais_deducoes_real)
            lista21.append(demais_deducoes_real)
        
        lista21 = lista21
        print('Demais_deducoes_real')
        print('Valor máximo: ',max(lista21))
        print('Valor mínimo: ',min(lista21))
        print('Quantidade de nulos:', nulos21)
        print()

        # 22
        lista22 = []     
       
        for y in dadosunidos1.collect():
            demais_deducoes_dolar = y[22]
            demais_deducoes_dolar = str(demais_deducoes_dolar).replace(',', '.')
            
            if demais_deducoes_dolar  == 'None':
                nulos22 += 1
                listao_nulos.append(nulos22)
            
            demais_deducoes_dolar  = str(demais_deducoes_dolar ).replace('None', '0.0')
            demais_deducoes_dolar  = float(demais_deducoes_dolar )
            lista22.append(demais_deducoes_dolar )

        lista22 = lista22
        print('Demais_deducoes_dolar')
        print('Valor máximo: ',max(lista22))
        print('Valor mínimo: ',min(lista22))
        print('Quantidade de nulos:', nulos22)
        print()

        # 23
        lista23 = []      
     
        for z in dadosunidos1.collect():
            pensao_militar_real = z[23]
            pensao_militar_real = str(pensao_militar_real).replace(',', '.')
            
            if pensao_militar_real   == 'None':
                nulos23 += 1
                listao_nulos.append(nulos23)
            
            pensao_militar_real = str(pensao_militar_real).replace('None', '0.0')
            pensao_militar_real = float(pensao_militar_real)
            lista23.append(pensao_militar_real)

        lista23 = lista23 
        print('Pensao_militar_real')
        print('Valor máximo: ',max(lista23))
        print('Valor mínimo: ',min(lista23))
        print('Quantidade de nulos:', nulos23)
        print()

        # 24
        lista24 = []     
      
        for um in dadosunidos1.collect():
            pensao_militar_dolar  = um[24]
            pensao_militar_dolar  = str(pensao_militar_dolar).replace(',', '.')
            
            if pensao_militar_dolar   == 'None':
                nulos24 += 1
                listao_nulos.append(nulos24)
            
            pensao_militar_dolar = str(pensao_militar_dolar  ).replace('None', '0.0')
            pensao_militar_dolar = float(pensao_militar_dolar  )
            lista24.append(pensao_militar_dolar)
            
        lista24 = lista24
        print('Pensao_militar_dolar')
        print('Valor máximo: ',max(lista24))
        print('Valor mínimo: ',min(lista24))
        print('Quantidade de nulos:', nulos24)
        print()

        # 25
        lista25 = []        
      
        for dois in dadosunidos1.collect():
            fundo_saude_real  = dois[25]
            fundo_saude_real  = str(fundo_saude_real).replace(',', '.')
            
            if fundo_saude_real   == 'None':
                nulos25 += 1
                listao_nulos.append(nulos25)
            
            fundo_saude_real = str(fundo_saude_real ).replace('None', '0.0')
            fundo_saude_real = float(fundo_saude_real )
            lista25.append(fundo_saude_real)

        lista25 = lista25
        print('Fundo_saude_real')
        print('Valor máximo: ',max(lista25))
        print('Valor mínimo: ',min(lista25))
        print('Quantidade de nulos:', nulos25)
        print()

        # 26
        lista26 = []     
      
        for tres in dadosunidos1.collect():
            fundo_saude_dolar = tres[26]
            fundo_saude_dolar = str(fundo_saude_dolar).replace(',', '.')
            
            if fundo_saude_dolar   == 'None':
                nulos26 += 1
                listao_nulos.append(nulos26)
            
            fundo_saude_dolar = str(fundo_saude_dolar).replace('None', '0.0')
            fundo_saude_dolar = float(fundo_saude_dolar)
            lista26.append(fundo_saude_dolar)

        lista26 = lista26
        print('Fundo_saude_dolar')
        print('Valor máximo: ',max(lista26))
        print('Valor mínimo: ',min(lista26))
        print('Quantidade de nulos:', nulos26)
        print()

        # 27
        lista27 = []
      
        for quatro in dadosunidos1.collect():
            taxa_ocupacao_imovel_funcional_real  = quatro[27]
            taxa_ocupacao_imovel_funcional_real  = str(taxa_ocupacao_imovel_funcional_real).replace(',', '.')
            
            if taxa_ocupacao_imovel_funcional_real == 'None':
                nulos27 += 1
                listao_nulos.append(nulos27)
            
            taxa_ocupacao_imovel_funcional_real = str(taxa_ocupacao_imovel_funcional_real).replace('None', '0.0')
            taxa_ocupacao_imovel_funcional_real = float(taxa_ocupacao_imovel_funcional_real)
            lista27.append(taxa_ocupacao_imovel_funcional_real)

        lista27 = lista27
        print('Taxa_ocupacao_imovel_funcional_real')
        print('Valor máximo: ',max(lista27))
        print('Valor mínimo: ',min(lista27))
        print('Quantidade de nulos:', nulos27)
        print()

        # 28
        lista28 = []      
    
        for cinco in dadosunidos1.collect():
            taxa_ocupacao_imovel_funcional_dolar  = cinco[28]
            taxa_ocupacao_imovel_funcional_dolar  = str(taxa_ocupacao_imovel_funcional_dolar).replace(',', '.')
            
            if taxa_ocupacao_imovel_funcional_dolar == 'None':
                nulos28 += 1
                listao_nulos.append(nulos28)
            
            taxa_ocupacao_imovel_funcional_dolar = str(taxa_ocupacao_imovel_funcional_dolar).replace('None', '0.0')
            taxa_ocupacao_imovel_funcional_dolar = float(taxa_ocupacao_imovel_funcional_dolar)
            lista28.append(taxa_ocupacao_imovel_funcional_dolar)
            
        lista28 = lista28    
        print('Taxa_ocupacao_imovel_funcional_dolar')
        print('Valor máximo: ',max(lista28))
        print('Valor mínimo: ',min(lista28))
        print('Quantidade de nulos:', nulos28)
        print()

        # 29
        lista29 = []      
     
        for seis in dadosunidos1.collect():
            remuneracao_deducoes_obrigatorias_real  = seis[29]
            remuneracao_deducoes_obrigatorias_real  = str(remuneracao_deducoes_obrigatorias_real).replace(',', '.')
            
            if remuneracao_deducoes_obrigatorias_real == 'None':
                nulos29 += 1
                listao_nulos.append(nulos29)
            
            remuneracao_deducoes_obrigatorias_real = str(remuneracao_deducoes_obrigatorias_real).replace('None', '0.0')
            remuneracao_deducoes_obrigatorias_real = float(remuneracao_deducoes_obrigatorias_real)
            lista29.append(remuneracao_deducoes_obrigatorias_real)
            
        lista29 = lista29
        print('Remuneracao_deducoes_obrigatorias_real')
        print('Valor máximo: ',max(lista29))
        print('Valor mínimo: ',min(lista29))
        print('Quantidade de nulos:', nulos29)
        print()

        # 30
        lista30 = []       
    
        for sete in dadosunidos1.collect():
            remuneracao_deducoes_obrigatorias_dolar  = sete[30]
            remuneracao_deducoes_obrigatorias_dolar  = str(remuneracao_deducoes_obrigatorias_dolar).replace(',', '.')
            
            if remuneracao_deducoes_obrigatorias_dolar == 'None':
                nulos30 += 1
                listao_nulos.append(nulos30)
            
            remuneracao_deducoes_obrigatorias_dolar = str(remuneracao_deducoes_obrigatorias_dolar).replace('None', '0.0')
            remuneracao_deducoes_obrigatorias_dolar = float(remuneracao_deducoes_obrigatorias_dolar)
            lista30.append(remuneracao_deducoes_obrigatorias_dolar)

        lista30 = lista30  
        print('Remuneracao_deducoes_obrigatorias_dolar')
        print('Valor máximo: ',max(lista30))
        print('Valor mínimo: ',min(lista30))
        print('Quantidade de nulos:', nulos30)
        print()

        # 31
        lista31 = []
       
        for oito in dadosunidos1.collect():
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_real  = oito[31]
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_real  = str(verbas_indenizatorias_registradas_sistemas_pessoal_civil_real).replace(',', '.')
            
            if verbas_indenizatorias_registradas_sistemas_pessoal_civil_real == 'None':
                nulos31 += 1
                listao_nulos.append(nulos31)
            
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_real = str(verbas_indenizatorias_registradas_sistemas_pessoal_civil_real).replace('None', '0.0')
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_real = float(verbas_indenizatorias_registradas_sistemas_pessoal_civil_real)
            lista31.append(verbas_indenizatorias_registradas_sistemas_pessoal_civil_real)

        lista31 = lista31
        print('Verbas_indenizatorias_registradas_sistemas_pessoal_civil_real')
        print('Valor máximo: ',max(lista31))
        print('Valor mínimo: ',min(lista31))
        print('Quantidade de nulos:', nulos31)
        print()

        # 32
        lista32 = []    
    
        for nove in dadosunidos1.collect():
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar  = nove[32]
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar  = str(verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar).replace(',', '.')
            
            if verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar == 'None':
                nulos32 += 1
                listao_nulos.append(nulos32)
            
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar = str(verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar).replace('None', '0.0')
            verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar = float(verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar)
            lista32.append(verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar)
            
        lista32 = lista32 
        print('Verbas_indenizatorias_registradas_sistemas_pessoal_civil_dolar')
        print('Valor máximo: ',max(lista32))
        print('Valor mínimo: ',min(lista32))
        print('Quantidade de nulos:', nulos32)
        print()

        # 33
        lista33 = []
    
        for dez in dadosunidos1.collect():
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_real  = dez[33]
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_real  = str(verbas_indenizatorias_registradas_sistemas_pessoal_militar_real).replace(',', '.')
            
            if verbas_indenizatorias_registradas_sistemas_pessoal_militar_real == 'None':
                nulos33 += 1
                listao_nulos.append(nulos33)
            
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_real = str(verbas_indenizatorias_registradas_sistemas_pessoal_militar_real).replace('None', '0.0')
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_real = float(verbas_indenizatorias_registradas_sistemas_pessoal_militar_real)
            lista33.append(verbas_indenizatorias_registradas_sistemas_pessoal_militar_real)

        lista33 = lista33
        print('Verbas_indenizatorias_registradas_sistemas_pessoal_militar_real')
        print('Valor máximo: ',max(lista33))
        print('Valor mínimo: ',min(lista33))
        print('Quantidade de nulos:', nulos33)
        print()
            
        # 34
        # Obs: Coluna com todos os valores zero.
        lista34 = []    
       
        for onze in dadosunidos1.collect():
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar = onze[34]
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar = str(verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar ).replace(',', '.')
            
            if verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar  == 'None':
                nulos34 += 1
                listao_nulos.append(nulos34)
            
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar  = str(verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar ).replace('None', '0.0')
            verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar  = float(verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar )
            lista34.append(verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar )

        lista34 = lista34
        print('Verbas_indenizatorias_registradas_sistemas_pessoal_militar_dolar ')
        print('Valor máximo: ',max(lista34))
        print('Valor mínimo: ',min(lista34))
        print('Quantidade de nulos:', nulos34)
        print()

        # 35
        lista35 = []   
     
        for doze in dadosunidos1.collect():
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real  = doze[35]
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real  = str(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real).replace(',', '.')
            
            if verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real == 'None':
                nulos35 += 1
                listao_nulos.append(nulos35)
            
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real = str(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real).replace('None', '0.0')
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real = float(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real)
            lista35.append(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real)

        lista35 = lista35
        print('Verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_real')
        print('Valor máximo: ',max(lista35))
        print('Valor mínimo: ',min(lista35))
        print('Quantidade de nulos:', nulos35)
        print()

        # 36
        lista36 = []      
       
        for treze in dadosunidos1.collect():
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar = treze[36]
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar = str(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar).replace(',', '.')
            
            if verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar == 'None':
                nulos36 += 1
                listao_nulos.append(nulos36)
            
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar = str(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar).replace('None', '0.0')
            verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar = float(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar)
            lista36.append(verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar)
        
        
        lista36 = lista36 
        print('Verbas_indenizatorias_programa_desligamento_voluntario_mp_792_2017_dolar')
        print('Valor máximo: ',max(lista36))
        print('Valor mínimo: ',min(lista36))
        print('Quantidade de nulos:', nulos36)
        print()

        # 37
        lista37 = []
        nulos37 = 0
      
        for quatorze in dadosunidos1.collect():
            total_verbas_indenizatorias_real = quatorze[37]
            total_verbas_indenizatorias_real = str(total_verbas_indenizatorias_real).replace(',', '.')
            
            if total_verbas_indenizatorias_real == 'None':
                nulos37 += 1
                listao_nulos.append(nulos37)
            
            total_verbas_indenizatorias_real = str(total_verbas_indenizatorias_real).replace('None', '0.0')
            total_verbas_indenizatorias_real = float(total_verbas_indenizatorias_real)
            lista37.append(total_verbas_indenizatorias_real)
        
        lista37 = lista37 
        print('Total_verbas_indenizatorias_real')
        print('Valor máximo: ',max(lista37))
        print('Valor mínimo: ',min(lista37))
        print('Quantidade de nulos:', nulos37)
        print()

        # 38
        lista38 = []
       
        for quinze in dadosunidos1.collect():
            total_verbas_indenizatorias_dolar = quinze[38]
            total_verbas_indenizatorias_dolar = str(total_verbas_indenizatorias_dolar).replace(',', '.')
            
            if total_verbas_indenizatorias_dolar == 'None':
                nulos38 += 1
                listao_nulos.append(nulos38)
            
            total_verbas_indenizatorias_dolar = str(total_verbas_indenizatorias_dolar).replace('None', '0.0')
            total_verbas_indenizatorias_dolar = float(total_verbas_indenizatorias_dolar)
            lista38.append(total_verbas_indenizatorias_dolar)
        
        lista38 = lista38 
        print('Total_verbas_indenizatorias_dolar')
        print('Valor máximo: ',max(lista38))
        print('Valor mínimo: ',min(lista38))
        print('Quantidade de nulos:', nulos38)
        print()
        
        
        df = pd.DataFrame(list(zip(lista0,lista1,lista2,lista3,lista4,lista5,lista7,lista9,
        lista13,lista15,lista17,lista23,lista25,lista29,lista33,lista37)), columns = ['ano',
        'mes','id servidor portal','cpf','nome',
        'remuneracao basica bruta','abate teto',
        'gratificacao natalina','ferias',
        'outras remuneracoes eventuais','irrf',
        'pensao militar','fundo saude',
        'remuneracao deducoes obrigatorias',
        'verbas indenizatorias registradas sistemas pessoal militar',
        'total verbas indenizatorias'])
      
                
    elif usuario == 'n':
        break
#-----------------------------------------------------------------------------------------------------------------

# TOTAL DE DADOS NULOS
print()

print('TOTAL DE DADOS NULOS:', sum(listao_nulos))

# RECRIANDO O ANTIGO DATAFRAME
for beta in range(0, 1):
    usuario2 = input('Deseja criar criar um novo csv [s/n]? ')
    
    if usuario == 's':
        df.to_csv("projeto_teste.csv", index = False)
        
    elif usuario == 'n':
        break

# ABRINDO O NOVO CSV COM SPARK
abrir_teste = spark.read.csv(r"projeto_teste.csv", header=True, inferSchema=True)


# PESQUISANDO PENSIONISTA POR NOME
nome_funcionario = input('Digite o nome do pensionista: ')

pesquisando_por_nome = abrir_teste.filter(abrir_teste.nome == f'{nome_funcionario}').show(truncate=False) 
