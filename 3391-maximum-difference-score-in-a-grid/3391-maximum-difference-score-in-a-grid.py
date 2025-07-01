class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('inf')]*n for _ in range(m)]
        max_score = -float('inf')
        dp[0][0] = grid[0][0]

        min_val = dp[0][0]
        for j in range(1,n):
            max_score = max(max_score, grid[0][j] - min_val)
            min_val = min(min_val, grid[0][j])
            dp[0][j] = min_val

        min_val = dp[0][0]
        for i in range(1,m):
            max_score = max(max_score, grid[i][0] - min_val)
            min_val = min(min_val, grid[i][0])
            dp[i][0] = min_val


        for i in range(1,m):
            for j in range(1,n):
                min_val = min(dp[i-1][j],  dp[i][j-1])
                max_score = max(max_score, grid[i][j] - min_val)
                min_val = min(dp[i-1][j],  dp[i][j-1], grid[i][j])
                dp[i][j] = min_val
        
        return max_score
        # 4 8 7
        # 6 3 10
        # 5 3 10
        # 8 8 3
