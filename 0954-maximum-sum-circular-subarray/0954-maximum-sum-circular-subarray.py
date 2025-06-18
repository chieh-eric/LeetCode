class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_max = [0]*n
        dp_min = [0]*n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1,n):
            dp_max[i] = max(dp_max[i-1]+nums[i],nums[i])
            dp_min[i] = min(dp_min[i-1]+nums[i],nums[i])
        
        if max(dp_max) < 0:
            return max(dp_max)
        else:
            return max(max(dp_max),sum(nums)-min(dp_min))
        #　 5 2 7 12 9 14