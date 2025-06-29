class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i = 0
        j = n // 2
        count = 0

        while i < n//2 and j < n:
            if 2*nums[i] <= nums[j]:
                count += 1
                i += 1
            j += 1
        return count*2
