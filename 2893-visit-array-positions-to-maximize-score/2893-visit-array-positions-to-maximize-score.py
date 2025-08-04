class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
       # 2 2 8 (8,4) 
       # 0 3 4 4 13
        if nums[0] % 2 == 0:
            max_even = nums[0]
            max_odd = float('-inf')  
        else:
            max_odd = nums[0]
            max_even = float('-inf')
            
        n = len(nums)
        for i in range(1,n):
            if nums[i] % 2 == 0:
                max_even = max(max_even + nums[i], max_odd + nums[i] - x)
            else:
                max_odd = max(max_odd + nums[i], max_even + nums[i] - x)



        return max(max_odd,max_even)
