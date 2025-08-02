class Solution(object):
    def longestLine(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        m = len(mat[0])

        visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]

        #print(visited)
        self.max_len = 0

        def dfs(i,j,k,l):
        
            self.max_len = max(self.max_len,l+1)
            
            visited[i][j][k] = True
            
            if k == 0:
                if i + 1 < n and not visited[i+1][j][k] and mat[i+1][j] == 1:
                    dfs(i+1,j,k,l+1)
            
            if k == 1:
                if j + 1 < m and not visited[i][j+1][k] and mat[i][j+1] == 1:
                    dfs(i,j+1,k,l+1)

            if k == 2:
                if j + 1 < m and i + 1 < n and not visited[i+1][j+1][k] and mat[i+1][j+1] == 1:
                    dfs(i+1,j+1,k,l+1)
            
            if k == 3:
                if j - 1 >= 0 and i + 1 < n and not visited[i+1][j-1][k] and mat[i+1][j-1] == 1:
                    dfs(i+1,j-1,k,l+1)


        for i in range(n):
            for j in range(m):
                for k in range(4):
                   
                    if not visited[i][j][k] and mat[i][j] == 1:
                        dfs(i,j,k,0)
        #print(visited)
        return self.max_len