class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def calculate(s):
            t = n
            count = t // s
            remain = t % s
            start = 1
            while t > 0:
                if remain:
                    minus = count + 1 
                    remain -= 1
                else:
                    minus = count
                start *= minus
                t -= minus
            return start
        
        max_val = 0
        for i in range(2,n+1):
            max_val = max(max_val,calculate(i))
        return max_val
        
