class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if i > 0 and mat[i][j] != 0:
                    mat[i][j] += mat[i-1][j]
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    min_h = mat[i][j]
                    for k in range(j, -1, -1):
                        if mat[i][k] == 0:
                            break
                        min_h = min(min_h, mat[i][k])
                        count += min_h
        return count
        # [[0, 1, 1, 0], 
        # [0, 2, 2, 1], 
        # [1, 3, 3, 0]]