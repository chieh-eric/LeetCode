class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [0]*(high+1)

        if zero == one:
            dp[zero] = 2
        else:
            dp[zero] = 1
            dp[one] = 1
        
        for i in range(min(zero,one)+1,high+1):
            dp[i] +=  dp[i-zero] % mod
            dp[i] +=  dp[i-one] % mod
        #print(dp)
        return sum(dp[low:high+1]) % mod
            