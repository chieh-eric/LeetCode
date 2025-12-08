class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        dp = [[float('inf')]* m for _ in range(n)]
        cur = 0
        for i in range(n):
            cur +=  grid[i][0]
            dp[i][0] = cur
        
        cur = 0
        for i in range(m):
            cur += grid[0][i]
            dp[0][i] = cur

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]