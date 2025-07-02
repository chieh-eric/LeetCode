class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [[0]*n for _ in range(2)]
        dp[0][1] = nums[0] + nums[1]
        dp[1][1] = nums[0] - nums[1]

        for i in range(2,n):
            dp[0][i] = max(dp[0][i-1],dp[1][i-1]) + nums[i]
            dp[1][i] = dp[0][i-1] - nums[i]
        return max(dp[0][n-1],dp[1][n-1])