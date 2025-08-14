class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 1
        right = n - 1

        while left < right:
            mid = (left+right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid 
                
            else:
                left = mid + 1
        return left

