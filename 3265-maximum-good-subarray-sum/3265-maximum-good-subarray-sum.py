from collections import defaultdict
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefix = 0
        seen = {}
        n = len(nums)
        max_sum = None

        for i in range(n):
            prefix += nums[i]

            for target in (nums[i]-k, nums[i]+k):
                if target in seen:
                    candidate = prefix - seen[target]
                    if max_sum is None or max_sum < candidate:
                        max_sum = candidate 

            prev = prefix - nums[i]
            if nums[i] not in seen or seen[nums[i]] > prev:
                seen[nums[i]] = prev
        return max_sum if max_sum else 0