class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        #print(nums)
        max_len = 1
        n = len(nums)
        left = 0
        cur = 0

        prefix = [0]*(n+1)
        val = 0
        for i, num in enumerate(nums):
            val += num
            prefix[i+1] = val
            
        #print(prefix)
        for right in range(n):
            cost = nums[right] * (right- left + 1) - (prefix[right+1] - prefix[left])
            
            while cost > k:
                left += 1
                cost = nums[right] * (right- left + 1) - (prefix[right+1] - prefix[left])
            
            max_len = max(max_len, right - left + 1)
        return max_len

