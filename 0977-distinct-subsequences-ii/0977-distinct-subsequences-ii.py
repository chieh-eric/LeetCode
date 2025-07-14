class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9+7
        n = len(s)
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            for j in range(i):
                if s[i] != s[j]:
                    dp[i] += dp[j]
            dp[i] += 1
            dp[i] %= mod
        return sum(dp) % mod