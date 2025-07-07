class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        min_val = 0
        max_val = -float('inf')
        for i in range(len(nums)):
            min_val = min(min_val, prefix)
            prefix += nums[i]
            max_val = max(max_val, prefix-min_val)
        return max_val