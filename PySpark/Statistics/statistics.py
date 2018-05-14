#Written for spark2.0 and higher

from pyspark import SparkContext
from pyspark.mllib.stat import Statistics
import random as rand
import numpy as np
from pyspark.mllib.linalg import Vectors, Matrices


def num_rand():
	return np.random.randn(1,4)

mat = sc.parallelize([num_rand(),num_rand(),num_rand(),num_rand()])

summary = Statistics.colStats(mat)

print(summary.mean())
print(summary.variance())
print(summary.numNonzeros())
print(summary.max())
print(summary.min())
print(summary.count())
print(summary.normL1())
print(summary.normL2())

#correlation
x = sc.parallelize(np.random.randn(4,1))
y = sc.parallelize(np.random.randn(4,1))
print("Correlation :",str(Statistics.corr(x,y)))

#Chi-square
#For Vector
x = Vectors.dense(np.random.random_sample((5)))
y = Vectors.dense(np.random.random_sample((5)))
chisqr = Statistics.chiSqTest(x,y)
print(chisqr.statistic)
print(chisqr.degreesOfFreedom)
print(chisqr.pValue)
print(chisqr.nullHypothesis)

# For Matrices
x = Matrices.dense(4,2,np.random.random_sample((8)))
y = Matrices.dense(4,2,np.random.random_sample((8)))
chisqr = Statistics.chiSqTest(x,y)
print(chisqr.statistic)
print(chisqr.degreesOfFreedom)
print(chisqr.pValue)
print(chisqr.nullHypothesis)