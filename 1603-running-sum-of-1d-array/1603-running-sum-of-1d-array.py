class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        cur = 0
        for num in nums:
            cur += num
            res.append(cur)
        return res