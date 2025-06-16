class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(arr)

        def find(array):
            l = len(array)
            dp = [0]*l
            dp[0] = array[0]
            for i in range(1,l):
                dp[i] = max(array[i],dp[i-1]+array[i])
            return max(dp)
        total = sum(arr)

        prefix_sum = cur = 0
        for i in range(n):
            cur += arr[i]
            prefix_sum = max(prefix_sum,cur)

        suffix_sum = cur = 0
        for i in range(n-1,-1,-1):
            cur += arr[i]
            suffix_sum = max(suffix_sum,cur)
  
        if k == 1:
            res = max(0,find(arr))
            return res % mod
        elif k == 2:
            return find(arr*2) % mod
        else:
            middle = max(0,(k-2)*total)
            front_and_back = max(prefix_sum+suffix_sum, find(arr))
            return (front_and_back + middle) % mod

        
