class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        n = len(nums)
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        return max(max(dic.values())*2-n,n%2)