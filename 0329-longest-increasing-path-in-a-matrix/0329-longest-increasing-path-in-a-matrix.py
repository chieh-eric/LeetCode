class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        dp = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if dp[i][j] != 0:
                return dp[i][j]

            lenght = 1
            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[i][j]:
                    lenght = max(lenght,1 + dfs(nx,ny))

            dp[i][j] = lenght
            return lenght
                
        for i in range(m):
            for j in range(n):
                longest = dfs(i,j)
                
                if longest > max_len:
                    max_len = longest
                    
        return max_len