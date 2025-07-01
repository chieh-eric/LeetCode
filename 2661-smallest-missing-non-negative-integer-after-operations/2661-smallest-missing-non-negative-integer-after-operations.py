from collections import defaultdict
class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        n = len(nums)
        dic = defaultdict(int)
        valid = set()
        for i in range(n):
            nums[i] = nums[i]%value
            dic[nums[i]] += 1
        
        i = 0
        while True:
            mod = i%value
            if dic[mod] == 0:
                return i
            dic[mod] -= 1
            i += 1
        return i