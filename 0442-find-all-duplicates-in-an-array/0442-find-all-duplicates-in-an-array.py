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
        bitMap = 0
        
        for val in nums:
            index = (1 << (val-1))
            if (index & bitMap) == 0:
                bitMap |= index
            else:
                ans.append(val)
        return ans
