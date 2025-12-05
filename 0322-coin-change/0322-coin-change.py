class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
          
            for val in coins:
                #print(i,val)
                if i - val >= 0:
                    dp[i] = min(dp[i] , dp[i-val] + 1)
        #print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
            

        # coins = [1,2,5]
        # counts = [3,4,5]
