class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach maintain dictionary
        # 0, 1, 2
        #    1
        # 3, 1, 2
        # 6, 4, 5
        # 9, 10, 8
        # 12 ,13, 14
        n = len(nums)
        # i -> At index, (0~2) represent the value after the mod 
        # dp[i][j] -> Maximum value of the current state
        dp = [[0]*3 for _ in range(n)]

        # Initialize
        dp[0][nums[0]%3] = nums[0] 
        for i in range(1, n):
            cur_val = nums[i]
            remain = cur_val % 3
            #print(dp)
            for j in range(3):
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                next_val = cur_val + dp[i-1][j]
                next_remain = next_val % 3
                dp[i][next_remain] = max(dp[i][next_remain], dp[i-1][next_remain], next_val)
            #print(dp)
                
        #print(dp)
        return dp[-1][0]

