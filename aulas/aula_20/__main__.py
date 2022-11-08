from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as B

spark = SparkSession.builder.appName("OTR").config("spark.sql.caseSensitive", "True").getOrCreate()
#Assim é pra importar com cabeçalho correto:
#df2 = spark.read.csv(r"C:\Users\Edimilza\Desktop\Engenharia_Dados\Atividade_16\Sistema_B_NoSQL.csv", header=True, inferSchema=True)

#Lendo os arquivos csv
df = spark.read.csv("Sistema_A_SQL.csv")
#print(df.show())
df1 = spark.read.csv("Sistema_B_NoSQL.csv")
#print(df1.show())
# print(df.dtypes)

# TRATAMENTOS:
df_concat = df.union(df1) #Concatenando as tabelas:
#df_concat.show()
print("-- ESTATISTICA USANDO DESCRIBE -------------------")
df_concat.describe().show() #mostra a estatistica

#df_concat.filter(df_concat['_c1'].isNull()).show() #Achou e imprimiu os nulos (limitado a qdt 20)
#df_concat.filter(df_concat['_c1'].isNull()).count() #Quantidade de valores nulos por campo
#df_concat = df_concat.na.drop() # Remove valores nulos do campo vendedor
print("------------------------")
print("O total de linhas é: ",df_concat.count()) #Imprime o total de linhas
print("------------------------")
print("-- MAX -----------------")
print("------------------------")
df_concat.groupBy("_c1").agg(B.max("_c2")).show()

print("------------------------")
print("-- MIN -----------------")
print("------------------------")
df_concat.groupBy("_c1").agg(B.min("_c2")).show()

print("------------------------")
print("-- SUN -----------------")
print("------------------------")
df_concat.groupBy("_c1").agg(B.sum("_c2")).show()

print("------------------------")
print("-- DESVIO PADRÃO -------")
print("------------------------")
df_concat.groupBy("_c1").agg(B.stddev("_c2")).show()

print("---------------------------------------")
print("-- ESTATISTICAS POR VENDEDOR ----------")
print("---------------------------------------")
# #estatisticas por vendedor:
df_concat.groupBy("_c1").agg(B.max("_c2"),B.sum("_c2"),B.count("_c2"), B.avg("_c2")).show() 
