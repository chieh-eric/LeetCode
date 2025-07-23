class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(multipliers)
        memo = {}
        def dp(left,index):
            if index == m:
                return 0
            if (left,index) in memo:
                return memo[(left,index)]
            right = n - 1 + left - index
            max_val = -float('inf')
            max_val = max(max_val, multipliers[index]*nums[left] + dp(left+1,index+1))
            max_val = max(max_val, multipliers[index]*nums[right] + dp(left,index+1))
            memo[(left,index)] = max_val
            return max_val
        
        return dp(0,0)