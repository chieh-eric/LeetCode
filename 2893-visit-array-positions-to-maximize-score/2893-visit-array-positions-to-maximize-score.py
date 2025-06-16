class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # dp[i] means the maximum score untill position i
        n = len(nums)
        dp = [0]* n

        dp[0] = nums[0]
        prev_odd = prev_even = -1
        if dp[0] % 2:
            prev_odd = 0
        else:
            prev_even = 0

        for i in range(1,n):
            max_val = -float('inf')
            if nums[i] % 2:
                if prev_odd != -1:
                    max_val = max(max_val,dp[prev_odd]+nums[i])
                if prev_even != -1:
                    max_val = max(max_val,dp[prev_even]+nums[i]-x)
                prev_odd = i
            else:
                if prev_odd != -1:
                    max_val = max(max_val,dp[prev_odd]+nums[i]-x)
                if prev_even != -1:
                    max_val = max(max_val,dp[prev_even]+nums[i])
                prev_even = i

            dp[i] = max_val
        return max(dp)