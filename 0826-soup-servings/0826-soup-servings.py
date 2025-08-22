class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        
        memo = {}

        def dp(a,b,p):
            if n > 5000:
                return 1
            if (a,b) in memo:
                return memo[(a,b)]
            
            if a <= 0 and b > 0:
                return p
            
            if a <= 0 and b <= 0:
                return 0.5*p
            
            if a > 0 and b <= 0:
                return 0

            res = dp(a-100, b, 0.25*p) + dp(a-75, b - 25, 0.25*p) + dp(a-50, b-50, 0.25*p) + dp(a-25, b-75, 0.25*p)
            memo[(a,b)] = res
            return res
        return dp(n,n,1)