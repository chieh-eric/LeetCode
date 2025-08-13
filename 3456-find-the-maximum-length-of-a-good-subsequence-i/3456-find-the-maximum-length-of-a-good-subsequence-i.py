from collections import defaultdict
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = defaultdict(lambda: [0]*(k+1))
        best = [0]*(k+1)

        for num in nums:
            arr = dp[num]
            new = arr[:]
            for i in range(k,-1,-1):
                same = arr[i] + 1
                change = best[i-1] + 1 if i > 0 else 0
                new[i] = max(same,change)
                best[i] = max(best[i], new[i])

            dp[num] = new
        return max(best)
                