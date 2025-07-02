import heapq
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        min_len = [float('inf')]*n
        left = 0
        cur = 0
        best = float('inf')
        res = float('inf')
        for right in range(n):
            cur += arr[right]
            
            while cur > target:
                cur -= arr[left]
                left += 1
            
            if cur == target:
                cur_length = right - left + 1
                if left > 0 and min_len[left-1] != float('inf'):
                    res = min(res, cur_length+min_len[left-1])

                best = min(best,cur_length)

            min_len[right] = best
        return res if res != float('inf') else -1