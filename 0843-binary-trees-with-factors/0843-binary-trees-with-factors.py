class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # dp[x] means when x being the root, the number of tree can build
        dp = {}
        n = len(arr)
        arr.sort()
        arr_set = set(arr)
        mod = 10**9 + 7
        for i in range(n):
            num = arr[i]
            dp[num] = 1
            for j in range(2,int(num**0.5)+1):
                if num % j == 0 and j in arr_set and (num//j) in arr_set:
                    if j == num // j:
                        dp[num] += dp[j]*dp[j]
                    else:
                        dp[num] += (dp[j]*dp[num//j]*2)
        #print(dp)
        return sum(dp.values()) % mod

