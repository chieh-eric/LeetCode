class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        mapper = {1:set([2,3,4,5,6]), 2:set([1,3,5]), 3:set([1,2,4,5]), 4:set([1,3,5]),5:set([1,2,3,4,6]),6:set([1,5])}
        mod = 10**9 + 7
        def dfs(prev1,prev2,index):
            if index == n:
                return 1
            if (prev1,prev2,index) in memo:
                return memo[(prev1,prev2,index)]
            
            cal = 0
            possible = mapper[prev2]
            for i in range(1,7):
                if i not in possible or i == prev1 or i == prev2:
                    continue
                cal += dfs(prev2,i,index+1) % mod
            memo[(prev1,prev2,index)] = cal % mod
            return cal % mod


        count = 0
        for i in range(1,7):
            count += dfs(None,i,1) % mod
        return count % mod