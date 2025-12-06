class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        dp = [[float('inf')]*3 for _ in range(n)]
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1, n):
            for j in range(3):
                if j == 0:
                    dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + costs[i][j]
                elif j == 1:
                    dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + costs[i][j]
                else:
                    dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + costs[i][j]
        return min(dp[-1])