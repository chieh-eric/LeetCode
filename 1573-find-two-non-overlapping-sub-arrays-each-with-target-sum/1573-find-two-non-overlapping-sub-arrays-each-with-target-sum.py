class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        n = len(arr)
        best = [float('inf')]*n
        min_val = float('inf')

        res = float('inf')
        cur = 0
        for right in range(n):
            cur += arr[right]

            while cur > target:
                cur -= arr[left]
                left += 1
            
            if cur == target:
                length = right - left + 1
                if left > 0 and best[left-1] != float('inf'):
                    res = min(res, best[left-1] + length)
                
                min_val = min(min_val, length)
            best[right] = min_val
        return res if res!=float('inf') else -1