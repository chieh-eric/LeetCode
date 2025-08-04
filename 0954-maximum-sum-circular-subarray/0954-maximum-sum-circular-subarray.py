class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_window = len(nums)
        max_sum = nums[0]
        cur = nums[0]

        
        n = len(nums)
        total = sum(nums)
        for i in range(1,n):
            cur = max(cur+nums[i],nums[i])
            max_sum = max(max_sum,cur)
        min_sum = nums[0]
        if max(nums) < 0:
            return max_sum
        cur = nums[0]
        for i in range(1,n):
            cur = min(cur+nums[i],nums[i])
            min_sum = min(min_sum,cur)
        print(min_sum)
        return max(max_sum, total-min_sum)
        # nums = nums + nums
        # print(nums)
        # left = 0
        # for right in range(len(nums)):

        # 5 -3 5 5 -3 5