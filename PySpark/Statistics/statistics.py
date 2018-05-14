#Written for spark2.0 and higher

from pyspark import SparkContext
from pyspark.mllib.stat import Statistics
import random as rand
import numpy as np

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