#usr/bin/python
#pyspark --packages com.databricks:spark-csv_2.10:1.4.0

from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator 
from pyspark.mllib.evaluation import RegressionMetrics

# Load training data
training = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('file:///home/pkatta/Downloads/spark/CASP.csv')

vecAssembler = VectorAssembler(inputCols=["F1", "F2", "F3","F5","F6","F7","F8","F9"], outputCol="features")
t = vecAssembler.transform(training)

(trainingData, testData) = t.randomSplit([0.7, 0.3])


lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8,featuresCol="features", labelCol="RMSD", predictionCol = "prediction")

lrModel = lr.fit(t)

# Print the coefficients and intercept for linear regression
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))

#valuator = RegressionEvaluator(predictionCol='prediction', labelCol='label')

