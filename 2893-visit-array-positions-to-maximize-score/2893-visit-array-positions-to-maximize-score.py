class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        max_even = max_odd = 0
        if nums[0] % 2 == 0:
            max_even = nums[0]
            max_odd = nums[0] - x
        else:
            max_even = nums[0] - x
            max_odd = nums[0]
        
        n = len(nums)
        for i in range(1,n):
            if nums[i] % 2 == 0:
                max_even = max(max_even, max_even+nums[i], max_odd + nums[i] - x)
            else:
                max_odd = max(max_odd, max_odd+nums[i], max_even + nums[i] - x)
           
        return max(max_even, max_odd)
       
