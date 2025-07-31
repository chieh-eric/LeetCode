class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for _ in range(n)]
       

        for j in range(m-2,-1,-1):
            for i in range(n):
                if i - 1 >= 0 and grid[i][j] < grid[i-1][j+1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1]+1)
                if grid[i][j] < grid[i][j+1]:
                    print("di")
                    dp[i][j] = max(dp[i][j], dp[i][j+1]+1)
                if i +1 < n and grid[i][j] < grid[i+1][j+1]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1]+1)
        #print(dp)
        val = [dp[i][0] for i in range(n)]
        return max(val)
                
        