import bisect
class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        arr = []
        n = len(nums)
        min_diff = float('inf')

        for i in range(x, n):
            bisect.insort(arr,nums[i-x])
            idx = bisect.bisect_left(arr, nums[i])

            if idx < len(arr):
                min_diff = min(min_diff, abs(nums[i] - arr[idx]))
            
            if idx > 0:
                min_diff = min(min_diff, abs(nums[i] - arr[idx-1]))
                
        return min_diff