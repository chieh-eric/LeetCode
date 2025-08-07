class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j]) 
                if j > 0:
                    dp[i][j] = min(dp[i][j-1],dp[i][j])
                dp[i][j] += grid[i][j]
        #print(dp)
        return dp[m-1][n-1]