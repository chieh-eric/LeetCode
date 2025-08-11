class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        # 1 2 3 5 6 10000
        n = len(stoneValue)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            res = -float('inf')
            res = max(res,stoneValue[i]-dp(i+1))
            if i + 1 < n:
                res = max(res,stoneValue[i] + stoneValue[i+1] - dp(i+2))
            if i + 2 < n:
                res = max(res,stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i+3))

            memo[i] = res
            return res
        ans = dp(0)
        #print(memo)
        #print(ans)
        if ans == 0:
            return "Tie"
        elif ans > 0:
            return "Alice"
        else:
            return "Bob"
