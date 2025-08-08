class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        n = len(nums)
        right =  n - 1

        while left < right:
            mid = (left+right) // 2

            if mid + 1 < n and nums[mid+1] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left