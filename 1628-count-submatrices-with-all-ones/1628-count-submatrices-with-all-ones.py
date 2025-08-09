class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        m = len(mat[0])
        right = [[0]*m for _ in range(n)]

        for i in range(n):
            count = 0
            for j in range(m-1,-1,-1):
                if mat[i][j] == 1:
                    count += 1
                else:
                    count = 0
                right[i][j] = count
     

        total = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    count = 0
                    min_val = float('inf')
                    for k in range(i,n):
                        if mat[k][j] == 1:
                            min_val = min(min_val,right[k][j])
                            count += min_val
                        else:
                            break
                    #print(count)
                    total += count
        return total
    