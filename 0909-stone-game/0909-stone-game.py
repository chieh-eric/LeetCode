class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i > j:
                return 0
            max_val = max(piles[i]-dfs(i+1,j), piles[j] - dfs(i,j-1))
            memo[(i,j)] = max_val
            return max_val
        
        if (dfs(0,len(piles)-1)) > 0:
            return True
            

            