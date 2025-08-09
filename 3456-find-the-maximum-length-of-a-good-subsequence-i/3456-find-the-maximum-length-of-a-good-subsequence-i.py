from collections import defaultdict
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # dp is a dictionary, key as the interger, value as ()
        dp = defaultdict(lambda: [0]*(k+1))
        best = [0]*(k+1)

        for x in nums:
            arr = dp[x]
            new = arr[:]

            for t in range(k, -1, -1):
                same = arr[t] + 1
                change = best[t-1] + 1 if t > 0 else 0
                new[t] = max(arr[t],same,change)
            dp[x] = new
            for i in range(k+1):
                best[i] = max(best[i],new[i])
        return max(best)