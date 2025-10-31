class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = []
        for num in nums:
            if num in dic:
                ans.append(num)
            else:
                dic[num] = True
        return ans