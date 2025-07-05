class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        # Use top-down dp with memorization
        def calculate((x1,y1),(x2,y2)):
            return abs(x1-x2) + abs(y1-y2)
        
        n = len(bikes)
        m = len(workers)
        dp = [[float('inf')]*(2**n) for _ in range(m)]

        memo = {}
        def dp(i, mask):
            if i == m:
                return 0
            if (i,mask) in memo:
                return memo[(i,mask)]
            res = float('inf')
            for j in range(n):
                if (mask&(1<<j)) == 0:
                    dist = calculate(bikes[j],workers[i])
                    res = min(res, dp(i+1,mask|(1<<j)) + dist) 
            memo[(i,mask)] = res
            return res
        return dp(0,0)