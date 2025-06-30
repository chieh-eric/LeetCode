class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # dp[i][j] means ending at position i, with k operation, the maximum length of good subsequence
        # Recursive form: dp[i][j] = max(dp[i-])
        n = len(nums)
        dp = [[1]*(k+1) for _ in range(n)]
        
        ans = 1 
        for i in range(n):
            for j in range(i):
                for t in range(k+1):
                    if nums[i] == nums[j]:
                        dp[i][t] = max(dp[i][t], dp[j][t]+1)
                    elif t > 0:
                        dp[i][t] = max(dp[i][t], dp[j][t-1]+1)
            ans = max(ans,max(dp[i]))
        return ans
