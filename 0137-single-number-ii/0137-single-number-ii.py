from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] == 3:
                del dic[num]
        return dic.items()[0][0]