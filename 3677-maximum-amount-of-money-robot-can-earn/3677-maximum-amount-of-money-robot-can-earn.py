class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        n = len(coins)
        m = len(coins[0])

        dp = [[[-float('inf')]*3 for _ in range(m)] for _ in range(n)]
        #print(dp)
        if coins[0][0] >= 0:
            for i in range(3):
                dp[0][0][i] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            for i in range(1,3):
                dp[0][0][i] = 0


        for i in range(n):
            for j in range(m):
                val = coins[i][j]
                for k in range(3):
                    if coins[i][j] >= 0:
                        if i > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        if j > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                    else:
                        if i > 0:
                            if k > 0:
                                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        if j > 0:
                            if k > 0:
                                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
        return max(dp[-1][-1])
                   