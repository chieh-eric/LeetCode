class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = -float('inf')
        prefix = 0
        min_prefix = {}
        n = len(nums)
        min_prefix[0] = 0

        for i in range(n):
            mod = (i+1) % k
            prefix += nums[i]

            if mod in min_prefix:
                max_val = max(max_val,prefix - min_prefix[mod] )


            if mod not in min_prefix:
                min_prefix[mod] = prefix
            else:
                min_prefix[mod] = min(min_prefix[mod],prefix)

        return max_val
            