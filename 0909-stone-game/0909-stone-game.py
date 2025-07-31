class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == j:
                return piles[i]
            
            val = max(piles[i]-dp(i+1,j), piles[j] - dp(i,j-1))
            memo[(i,j)] = val
            return val
        return True if dp(0,len(piles)-1) > 0 else False
            