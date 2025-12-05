class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, val in enumerate(nums):
            if val in dic:
                return [dic[val], i]
            dic[target-val] = i
        