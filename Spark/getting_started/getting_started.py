from pyspark import SparkContext, SparkConf
import random as rand
conf = SparkConf().setAppName("getting_started")
sc = SparkContext(conf=conf)
data = rand.sample(range(1000),10)
distData = sc.parallelize(data)
print("++++++++++++++++++++++++++")
print(distData)
txtFile = sc.textFile("file:///home/pkatta/Spark_Session/shakespeare.txt")
txtFile.persist()

if __name__ = "__main__":
	def myFunc(s):
		words = s.split(" ")
		return len(words)

txtFile.map(myFunc).reduce(lambda a,b: a+b)

print(txtFile.first())
#counts the total no of lines in the given txt file
print(txtFile.map(lambda s: len(s)).reduce(lambda a, b: a + b))

#Saving and loading sequence files
rdd = sc.parallelize(range(1,4)).map(lambda x:(x,"a" * x))
rdd.saveAsSequenceFile("file:///home/pkatta/Spark_Session/rdd")
print("++++++++++++++++++++++++++")
sorted(sc.sequenceFile("file:///home/pkatta/Spark_Session/rdd").collect())

rdd.first()
