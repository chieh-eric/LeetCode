from collections import defaultdict
class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = [[ defaultdict(int) for _ in range(m)]for _ in range(n)]
        dp[0][0][grid[0][0]] += 1
        count = 0

        for i in range(n):
            for j in range(m):
                for key in dp[i][j]:
                    count = dp[i][j][key]

                    if i + 1 < n:
                        dp[i+1][j][grid[i+1][j]^key] += count % mod
                    
                    if j + 1 < m:
                        dp[i][j+1][grid[i][j+1]^key] += count % mod
        #print(dp)
        return dp[n-1][m-1][k] % mod