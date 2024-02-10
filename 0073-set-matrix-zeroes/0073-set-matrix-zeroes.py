class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = False
        col = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][0] == 0:
                    col = True
                if matrix[0][j] == 0:
                    row = True 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1,len(matrix),1):
            for j in range(1,len(matrix[0]),1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[0][0] == 0:  
                    if row:
                        matrix[0][j] = 0
                    if col:
                        matrix[i][0] = 0
                    
