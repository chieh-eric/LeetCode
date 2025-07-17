from collections import defaultdict
class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        last_pos = {}
        n = len(nums)
        for i in range(n):
            last_pos[nums[i]] = i
        res = 0
        end = 0
        for i in range(n):
            end = max(end,last_pos[nums[i]])
            if i == end:
                res += 1 % mod
        return 2**(res-1) % mod