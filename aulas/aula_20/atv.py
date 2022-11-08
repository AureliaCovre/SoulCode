from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("OTR").config("spark.sql.caseSensitive", "True").getOrCreate()
#Assim é pra importar com cabeçalho correto:
#df2 = SparkSession.read.csv(r"C:\Users\Cleberson\Downloads\EmendasParlamentares\Emendas.csv", header=True, inferSchema=True)

#Lendo os arquivos csv
emenda = spark.read.csv("Emendas.csv")
#print(emenda.show())
print(emenda.count()) #Imprime o total de linhas
