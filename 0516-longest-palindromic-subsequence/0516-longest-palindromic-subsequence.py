class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)] # dp means the maximum length between i, j
        
        
        for length in range(1, n+1):
            for i in range(n-length + 1):
                r = i + length - 1
                if length == 1:
                    dp[i][r] = 1
                elif length == 2:
                    if s[i] == s[r]:
                        dp[i][r] = 2
                    else:
                        dp[i][r] = 1
                else:
                    if s[i] == s[r]:
                        dp[i][r] = dp[i+1][r-1] + 2
                    else:
                        dp[i][r] = max(dp[i+1][r], dp[i][r-1])
        return dp[0][-1]
                