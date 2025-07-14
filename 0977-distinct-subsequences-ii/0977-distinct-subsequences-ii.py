class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9+7
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        last = {}
        for i in range(n):
            ch = s[i]
            dp[i+1] = (2*dp[i]) % mod
            if s[i] in last:
                dp[i+1] = (dp[i+1] - dp[last[s[i]]]) % mod
            last[s[i]] = i
        return (dp[n] - 1) % mod