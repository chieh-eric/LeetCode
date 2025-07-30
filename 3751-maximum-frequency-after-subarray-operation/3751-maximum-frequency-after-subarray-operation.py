from collections import defaultdict
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        orig = nums.count(k)
        max_gain = 0
        for i in range(1,51):
            if i == k:
                continue
            max_count = cur_count = 0
            for num in nums:
                if num == i:
                    cur_count += 1
                elif num == k:
                    cur_count -= 1
                
                cur_count = max(cur_count,0)
                max_count = max(max_count,cur_count)
            max_gain = max(max_gain,max_count)
        return max_gain + orig

                