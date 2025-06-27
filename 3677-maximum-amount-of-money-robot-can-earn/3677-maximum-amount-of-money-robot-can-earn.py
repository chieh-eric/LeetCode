class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float('inf')]*3 for _ in range(n)]for _ in range(m)]

        if coins[0][0] > 0:
            for k in range(3):
                dp[0][0][k] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    val = coins[i][j]
                    if i > 0:
                        if val > 0:
                            dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k]+val)
                        else:
                            if k > 0:
                                dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k-1])
                            dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k]+val)
                    if j > 0:
                        if val > 0:
                            dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k]+val)
                        else:
                            if k > 0:
                                dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1])
                            dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k]+val)
                            
        return max(dp[m-1][n-1][0],dp[m-1][n-1][1],dp[m-1][n-1][2])