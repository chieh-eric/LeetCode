class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False]*n
        for i in range(n):
            if i >= 1:
                # Criteria 1 
                if i == 1:
                    if nums[i] == nums[i-1]:
                        dp[i] = True
                else:
                    if nums[i] == nums[i-1] and dp[i-2]:
                        dp[i] = True
                
            if i >= 2:
                # Criteria 2
                if i == 2:
                    if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                        dp[i] = True
                else:
                    if nums[i] == nums[i-1] and nums[i-1] == nums[i-2] and dp[i-3]:
                        dp[i] = True
                
                # Criteria 3
                if i == 2:
                    if nums[i] == nums[i-1] + 1 and nums[i-1] == nums[i-2] + 1:
                        dp[i] = True
                else:
                    if nums[i] == nums[i-1] + 1 and nums[i-1] == nums[i-2] + 1 and dp[i-3]:
                        dp[i] = True
        return dp[-1]
                

