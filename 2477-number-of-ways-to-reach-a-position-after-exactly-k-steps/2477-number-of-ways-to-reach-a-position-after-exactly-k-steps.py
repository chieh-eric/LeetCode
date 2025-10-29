class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        # Standardize startPos and endPos
        start = 0
        end = endPos - startPos
        mod = 10**9 + 7

        if (k - end) % 2 or end > k:
            return 0

        memo = {}
        def dfs(distance , step):
            if distance >= step or step <= 0:
                return int(distance == step)
            if (distance, step) in memo:
                return memo[(distance, step)]

            total = dfs(distance-1, step-1) + dfs(distance+1, step-1)
            memo[(distance, step)] = total % mod
            return total % mod
        
        return dfs(end, k) % mod

        

        
