import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        a = np.array(matrix).transpose()
        a = np.rot90(matrix,3)
        
        for i in range(l):
            for j in range(l):
                matrix[i][j] = int(a[i][j])
        #print(len(a))
        #matrix = matrix.transpose()
        #print(matrix)