class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1, min(n, i+nums[i]+1)):
                dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]
