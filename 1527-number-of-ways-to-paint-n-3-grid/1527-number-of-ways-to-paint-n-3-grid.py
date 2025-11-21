class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Use, dp[i][j][color] -> number valid way at this point
        # ABA
        # BAB, BAC, CAC, BCB, BAC, CAB
        aba = 6
        abc = 6
        mod = 10**9 + 7

        for i in range(n-1):
            aba, abc = aba*3 + abc*2, abc*2 + aba*2

        return (aba + abc) % mod
        