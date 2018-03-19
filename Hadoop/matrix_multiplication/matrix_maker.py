#!/usr/bin/env python
import numpy as np

print("Give m,n,p value in m x n for matrix A and in n x p for matrix B seperated by comma")
m,n,p = input()

A = np.int_(10 * np.random.rand(int(m),int(n))).reshape(m,n)

B = np.int_(10 * np.random.rand(int(n),int(p))).reshape(n,p)

#C = np.matmul(A,B)

def writeToText(matrixA,matrixB,matrix_nameA,matrix_nameB):
	f = open("matrixA.txt","w+")
	f.write(str(m)+" "+str(n))
	for i in range(m):
		for j in range(n):
			f.write("\n"+str(i)+","+str(j)+","+str(matrix_nameA)+","+str(matrixA[i][j]))
			print(i,j,matrix_nameA,matrixA[i][j])
	f.close()
	f = open("matrixB.txt","w+")
	f.write(str(n)+" "+str(p))
	for i in range(n):
		for j in range(p):
			f.write("\n"+str(i)+","+str(j)+","+str(matrix_nameB)+","+str(matrixB[i][j]))
			print(i,j,matrix_nameB,matrixB[i][j])
	f.close()
	'''for i in range(m):
		for j in range(p):
			f.write(str(i)+","+str(j)+","+str(matrix_nameC)+","+str(matrixC[i][j])+"\n")
			print(i,j,matrix_nameC,matrixC[i][j])
	'''		
#writeToText(A,B,C,"A","B","C")
writeToText(A,B,"A","B")