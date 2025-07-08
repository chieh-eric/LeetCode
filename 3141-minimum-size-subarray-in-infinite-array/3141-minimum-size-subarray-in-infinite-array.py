class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        k = target // total
        remain = target % total

        arr = nums + nums
        min_len = float('inf')
        size = 0
        left = 0
        for right in range(2*n):
            size += arr[right]
            while size > remain:
                size -= arr[left]
                left += 1
            if size == remain:
                min_len = min(min_len, right - left + 1)
        return k*n + min_len if min_len != float('inf') else -1