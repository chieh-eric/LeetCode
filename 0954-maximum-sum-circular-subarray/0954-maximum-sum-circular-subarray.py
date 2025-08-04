class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = min_sum = nums[0]
        cur = nums[0]
        n = len(nums)
        total = sum(nums)
        # Find original largest
        for i in range(1,n):
            cur = max(cur+nums[i],nums[i])
            max_sum = max(max_sum,cur)

        if max(nums) < 0:
            return max_sum

        # Find the circular largest
        cur = nums[0]
        for i in range(1,n):
            cur = min(cur+nums[i],nums[i])
            min_sum = min(min_sum,cur)

        return max(max_sum, total-min_sum)
       