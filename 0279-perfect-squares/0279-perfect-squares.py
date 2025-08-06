class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # memo = {}
        # def dfs(val):
        #     if (val**0.5).is_integer():
        #         memo[val] = 1
        #         return 1

        #     min_op = float('inf')
        #     if val in memo:
        #         return memo[val]
            
        #     for i in range(1,int(val**0.5)+1):
        #         min_op = min(min_op, dfs(val-i**2) + 1)
            
        #     memo[val] = min_op
        #     return min_op
        # return dfs(n)

        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i],dp[i-(j*j)] + 1)
                j += 1
        #print(dp)
        return dp[n]
