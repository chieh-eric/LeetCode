class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0]*(n+1)

        for i in range(1,n+1):
            max_val = arr[i-1]
            for j in range(1,k+1):
                if i - j < 0:
                    break
                max_val = max(max_val, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + max_val*j)
        #print(dp)
        return dp[n]