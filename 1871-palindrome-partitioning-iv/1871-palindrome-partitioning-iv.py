class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for length in range(1,n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]



        for i in range(n-2):
            if not dp[0][i]:
                continue
            for j in range(i+1,n-1):
                if not dp[i+1][j]:
                    continue
                if dp[j+1][n-1]:
                    return True
        return False
