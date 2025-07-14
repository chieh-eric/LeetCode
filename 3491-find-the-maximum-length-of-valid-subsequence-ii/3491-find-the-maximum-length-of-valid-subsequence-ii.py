class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # define dp[i][mod] means ending at index i whith the mod value mod
        n = len(nums)
        dp = [[0]*k for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(i):
                mod = (nums[i]+nums[j]) % k
                dp[i][mod] = max(dp[i][mod],dp[j][mod]+1)
                ans = max(ans,dp[i][mod])
        #print(dp)
        return ans + 1