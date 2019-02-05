import numpy as np
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l = len(board)
        
        r = [0,0,0,1,1,1,2,2,2]
        c = []
               
        
        b = np.array(board)
        b = b.transpose()
        
        board = [[s.encode('ascii') for s in list] for list in board]
        b = [[s.encode('ascii') for s in list] for list in b]

        for j in range(l):
            temp = [i for i in board[j] if i != '.']        
            if len(set(temp)) != len(temp):
                return False

            temp = [i for i in b[j] if i != '.']        
            if len(set(temp)) != len(temp):
                return False            
        

        for i in [0,3,6]:
            for j in [0,3,6]:
                temp = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                temp = [a for a in temp if a != '.']
                if len(set(temp)) != len(temp):
                    return False

        return True    

        #print(x[:] = (value for value in x if value != 2))
        #temp = list(filter(lambda a: a != '.', board[0]))        
        #print(temp)

        #b = np.array(board)
        #b = b.transpo

        #for i in range(len(board)):
            #print(board[i].remove(u'.'))
            #print(board[i].remove("."))
        #print(b.transpose()[1])