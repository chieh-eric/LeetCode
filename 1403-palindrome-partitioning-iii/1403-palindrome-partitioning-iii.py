class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k == n :
            return 0
        
       

        dp = [[float('inf')]*(n) for _ in range(n)] # Start at index i, with lenght j, number of op to make to palindrome
        for length in range(1,n+1):
            for i in range(n- length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    if length <= 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i+1][j-1]

        #print(dp)
        memo = {}

        def dfs(i,j,split):
            if split == 1:
                return dp[i][j]
            if (i,j,split) in memo:
                return memo[(i,j,split)]

            min_cost = float('inf')
            for u in range(i,j-split+2):
                cost = dp[i][u] + dfs(u+1,j,split-1)
                min_cost = min(min_cost,cost)
                memo[(i,j,split)] = min_cost

            return min_cost

        
        return dfs(0,n-1,k)