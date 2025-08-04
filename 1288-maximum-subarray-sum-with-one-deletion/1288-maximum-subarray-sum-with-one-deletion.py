class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[0]*2 for i in range(n)]
        dp[0][0] = arr[0]
        max_val = arr[0]
        for i in range(1,n):
            dp[i][0] = max(arr[i], arr[i] + dp[i-1][0])
            dp[i][1] = max(dp[i-1][0], arr[i] + dp[i-1][1])
            max_val = max(max_val, dp[i][0], dp[i][1])
        #print(dp)
        return max_val