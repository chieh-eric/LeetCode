class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        # AND
        # If 0 -> OR
        # Record in ans
        for val in nums:
            idx = abs(val) - 1
            if nums[idx] < 0:
                ans.append(abs(val))
            else:
                nums[idx] = -nums[idx]
        return ans
