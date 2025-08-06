class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dfs(v):
            if v == 0:
                return 0
            
            if v == 1:
                return 1
            
            if v == 2:
                return 1
            
            if v in memo:
                return memo[v]
            
            val1 = dfs(v-1)
            val2 = dfs(v-2)
            val3 = dfs(v-3)

            memo[v] = val1 + val2 + val3
            
            return  val1 + val2 + val3
        
        return dfs(n)