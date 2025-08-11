class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        squares = [val**2 for val in range(1,int(sqrt(n))+1)]
        #print(squares)
        dp = [0]*(n+1)
        dp[0] = False

        for i in range(1,n+1):
            
            win = False
            for s in squares:
                if s > i:
                    break
                if not dp[i-s]:
                    win = True
                    break
            dp[i] = win
        return dp[n]
