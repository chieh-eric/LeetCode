class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = min_val = cur_max = cur_min = nums[0]
        n = len(nums)
        for i in range(1,n):
            cur_max = max(nums[i], cur_max + nums[i])
            cur_min = min(nums[i], cur_min + nums[i])

            max_val = max(max_val,cur_max)
            min_val = min(min_val,cur_min)
        
        total = sum(nums)
        if min_val == total:
            return max_val
        
        return max(max_val, total-min_val)
        