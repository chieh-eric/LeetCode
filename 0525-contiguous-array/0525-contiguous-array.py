class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int] 
        :rtype: int
        """
        max_len = 0
        dic = {}
        dic[0] = -1
        cur = 0
        for i, num in enumerate(nums):
            if num == 0:
                num = -1
            cur += num
            if cur in dic:
                max_len = max(max_len, i - dic[cur])
            else:
                dic[cur] = i
        return max_len