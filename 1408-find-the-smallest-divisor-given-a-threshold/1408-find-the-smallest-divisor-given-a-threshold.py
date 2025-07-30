class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums)

        def calculate(val):
            total = 0
            for num in nums:
                total = total + ((num+val-1) // val)
         
            return total

        while left < right:        
            mid = (left+right) // 2
            res = calculate(mid)
          
            if res > threshold:
                left = mid + 1
            else:
                right = mid
        return left