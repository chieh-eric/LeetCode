class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        direciton = [(0,1),(1,0)]
        n = len(grid)
        m = len(grid[0])
        
        dp = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]
        

        dp[0][0][0] = 0
        cur_cost = 0
        for i in range(1, n):
            c = 0 if grid[i][0] == 0 else 1
            if cur_cost+c <= k:
                dp[i][0][cur_cost+c] = dp[i-1][0][cur_cost] + grid[i][0]
            cur_cost += c

        cur_cost = 0
        for j in range(1, m):
            c = 0 if grid[0][j] == 0 else 1
            if cur_cost+c <= k:
                dp[0][j][cur_cost+c] = dp[0][j-1][cur_cost] + grid[0][j]
            cur_cost += c
            

        #print(dp)
        for i in range(1, n):
            for j in range(1, m):
                cost = 0 if grid[i][j] == 0 else 1
                score = grid[i][j]
                for c in range(k+1):
                    if dp[i-1][j][c] != -1:
                        if c + cost <= k:
                            dp[i][j][c + cost] = max(dp[i][j][c + cost], dp[i-1][j][c] + score)
                            
                    if dp[i][j-1][c] != -1:
                        if c + cost <= k:
                            dp[i][j][c + cost] = max(dp[i][j][c + cost], dp[i][j-1][c] + score)
                   
        #print(dp)
                    
                
        


        return max(dp[-1][-1])
        