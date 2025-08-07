class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        total = sum(arr)
        max_val = 0
        min_val = float('inf')
        n = len(arr)
        cur_max = cur_min = 0
        for i in range(len(arr)):
            cur_max = max(arr[i],cur_max+arr[i])
            cur_min = min(arr[i],cur_min+arr[i])

            max_val = max(max_val, cur_max)
            min_val = min(min_val, cur_min)
        prefix = suffix = 0
        cur = 0
        for i in range(n):
            cur += arr[i]
            prefix = max(prefix,cur)
        cur = 0
        for i in range(n-1,-1,-1):
            cur += arr[i]
            suffix = max(suffix,cur)
        
        if k == 1:
            return max_val
        if k == 2:
            return max(max_val, total - min_val,  total*k) % mod
        if min_val == total:
            return max_val
        
        return max(max_val, total*(k-2) + prefix + suffix, total - min_val, total*k) % mod

