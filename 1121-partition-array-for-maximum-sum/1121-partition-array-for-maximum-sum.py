class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0]*(n+1)
        dp[1] = arr[0]

        for i in range(2,n+1):

            for j in range(1,k+1):
                if i - j < 0:
                    break
                dp[i] = max(dp[i], dp[i-j] + max(arr[i-j:i])*j)
        #print(dp)
        return dp[n]