class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        # dp[i] means the maximum scores can earn, start from index i
        # Two choices, 1. Selcet -> dp[i] = dp[i+skip+1] + points, 2.Not select -> dp[i] = dp[i+1]
        # Start from right to left
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            points, skip = questions[i]
            if i + skip + 1 < n:
                
                dp[i] = max(dp[i+1],dp[i + skip + 1 ] + points)
            else:
                dp[i] = max(dp[i+1],points)
        return dp[0]