import bisect
class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # [4] , min_val = 2
        # [3,4], min_val = 0
        sort_list = []
        min_val = float('inf')
        for i, val in enumerate(nums):
            if i < x:
                continue
            new_element = nums[i-x]
            insort(sort_list, new_element)
            idx = bisect.bisect_left(sort_list,val)
            #print(sort_list, val)

            if idx < len(sort_list):
                min_val = min(min_val, abs(val - sort_list[idx]))
            
            if idx > 0:
                min_val = min(min_val, abs(val-sort_list[idx-1]))
        return min_val

        