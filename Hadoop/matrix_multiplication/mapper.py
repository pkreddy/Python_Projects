#!/usr/bin/env python

Ar = 0
Ac = 0
Br = 0
Bc = 0

f = open("matrixA.txt","r")
Ar,Ac = map(int,f.readline().split())
#print(Ar,Ac)

f1 = open("matrixB.txt","r")
Br,Bc = map(int,f1.readline().split())
#print(Br,Bc)

for pos,line in enumerate(f):
	#print(pos,line)
	for i in range(Bc):
		print("%s,%s %s,%s,%s" % (int(line.split(",")[0]),i,'A',int(line.split(",")[1]),int(line.split(",")[3])))
f.close()

for pos,line in enumerate(f1):
	#print(pos,line)
	for i in range(Ar):
		print("%s,%s %s,%s,%s" % (i,int(line.split(",")[1]),'B',int(line.split(",")[0]),int(line.split(",")[3])))
f1.close()
