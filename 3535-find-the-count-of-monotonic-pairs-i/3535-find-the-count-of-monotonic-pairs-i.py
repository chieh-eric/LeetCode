class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use dp, dp[i][x] means untill the length i, the valid pair of arr1[i] == x
        # nums[i-1] - prev >= nums[i] - x
        n = len(nums)
        dp = [[0]*(max(nums)+1) for _ in range(n)]
        mod = 10**9 + 7
        for i in range(nums[0]+1):
            dp[0][i] = 1

        for i in range(1,n):
            for prev in range(nums[i-1]+1):
                if dp[i-1][prev] == 0:
                    continue
                
                upper = nums[i]
                lower = max(prev,nums[i] - (nums[i-1]-prev))
                for k in range(lower,upper+1):
                    dp[i][k] += dp[i-1][prev]
                    dp[i][k] %= mod
        
        return sum(dp[n-1][x] for x in range(nums[n-1]+1)) % mod
