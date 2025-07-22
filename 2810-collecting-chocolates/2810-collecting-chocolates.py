class Solution(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # dp[i] means the minimum cost to select
        n = len(nums)
        min_cost = min(nums)
        min_index = nums.index(min_cost)
        cur = nums[::]
        prev = sum(cur)
        for rotate in range(1,n+1):
            for i in range(n-1,-1,-1):
               
                cur[i] = min(cur[i],nums[(i-rotate)%n])
            if prev < sum(cur)+x*rotate:
                return prev
            prev = sum(cur)+x*rotate
    
