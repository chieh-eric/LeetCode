class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0]*n for _ in range(m)]
       
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -float('inf')
        dp[0][0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = max(dp[0][i-1],0)
        
        for i in range(1,m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = max(dp[i-1][0],0)
        

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] == 0:
                    left = dp[i][j-1] if dp[i][j-1] != -float('inf') else 0
                    up = dp[i-1][j] if dp[i-1][j] != -float('inf') else 0
                    dp[i][j] = left+up
        #print(dp)
        return dp[m-1][n-1] if dp[m-1][n-1] != -float('inf') else 0

        #[[0,0,0],
        # [0,1,0],
        # [0,0,0]