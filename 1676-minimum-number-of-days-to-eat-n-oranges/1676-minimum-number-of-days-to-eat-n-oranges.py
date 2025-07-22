class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dfs(day):
            if day == 0:
                return 0
            if day == 1:
                return 1
            if day == 2 or day == 3:
                return 2
            if day in memo:
                return memo[day]

            min_val = float('inf')
            min_val = min(min_val,dfs(day%2)+dfs(day//2))
            min_val = min(min_val,dfs(day%3)+dfs(day//3))
            memo[day] = 1 + min_val
            return 1 +min_val
        return dfs(n)