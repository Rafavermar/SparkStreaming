import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

# Configurar la ubicación de WINUTILS.EXE
conf = SparkConf().set("spark.hadoop.winutils.path", "Ruta\\al\\directorio\\del\\proyecto\\con\\WINUTILS.EXE")

# Crear una sesión Spark
sc = SparkContext(appName="MiAplicacionSpark", conf=conf)


def start_streaming(spark):
    stream_df = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

    query = stream_df.writeStream.outputMode("append").format("console").start()
    query.awaitTermination()


if __name__ == "__main__":
    spark_conn = SparkSession.builder.appName("SocketStreamConsumer").getOrCreate()

    start_streaming(spark_conn)
