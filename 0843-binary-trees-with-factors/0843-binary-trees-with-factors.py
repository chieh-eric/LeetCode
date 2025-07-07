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
            for left in arr:
                if left > int(num**0.5):
                    break
                if num % left == 0 and (num//left) in arr_set:
                    if left == num // left:
                        dp[num] += dp[left]*dp[left]
                    else:
                        dp[num] += (dp[left]*dp[num//left]*2)
                
        print(dp)
        return sum(dp.values()) % mod

