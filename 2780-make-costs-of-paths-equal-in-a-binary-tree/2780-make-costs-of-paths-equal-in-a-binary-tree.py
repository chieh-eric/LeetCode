class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        self.ans = 0

        def dfs(i):
            if 2*i > n:
                return cost[i-1]
            
            left = dfs(2*i)
            right = dfs(2*i+1)
            self.ans += abs(left-right)
            return cost[i-1] + max(left,right)
        dfs(1)
        return self.ans