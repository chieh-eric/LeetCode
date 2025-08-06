class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0] = 1
        nums.sort()
        n = len(nums)

        for i in range(target+1):
            j = 0
            while j < n and nums[j] <= i:
                dp[i] += dp[i-nums[j]]
                j += 1
        #print(dp)
        return dp[target]