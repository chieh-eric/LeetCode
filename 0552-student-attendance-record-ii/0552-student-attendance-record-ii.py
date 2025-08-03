import math
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [[0]*3 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            # if adding p
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
            
            # if adding l
            dp[i][1] = dp[i-1][0] % mod
            dp[i][2] = dp[i-1][1] % mod
       #print(dp)
        count = 0
        # case A, if a in i, left = i , right = n - i - 1
        for i in range(n):
            left_valid = (dp[i][0] + dp[i][1] + dp[i][2]) % mod
            right_valid = (dp[n-i-1][0] + dp[n-i-1][1] + dp[n-i-1][2]) % mod
            
            count += (left_valid*right_valid) % mod
        return (count + sum(dp[n])) % mod



        