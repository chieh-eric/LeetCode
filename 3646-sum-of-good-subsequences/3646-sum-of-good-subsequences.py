from collections import defaultdict
class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        dp = defaultdict(int) # count number of ways when reach nums[i] at ending
        sum_dp = defaultdict(int) # count sum when nums[i] at the end

        for num in nums:
            dp[num] += dp[num-1] + dp[num+1] + 1
            dp[num] %= mod

            sum_dp[num] += sum_dp[num-1] + sum_dp[num+1] + num*(dp[num-1] + dp[num+1] + 1)
            sum_dp[num] %= mod
        
        return sum(sum_dp.values()) % mod