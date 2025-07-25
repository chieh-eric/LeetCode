class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = {0:True}
        n = len(stones)
        total = sum(stones)
        target = total // 2
        for num in stones:
            current = dp.copy()
            for key in current:
                if key + num <= target:
                    dp[key+num] = True
        
        
        return total - 2*max(dp)