class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])

        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = points[0][i]

        for i in range(1,m):
            left = [0]*n
            right = [0]*n
            prev = dp[i-1]
            left[0] = prev[0]
            for j in range(1,n):
                left[j] = max(left[j-1]-1, prev[j])
            
            right[n-1] =  prev[n-1]
            for j in range(n-2,-1,-1):
                right[j] = max(right[j+1]-1, prev[j])
           
            for j in range(n):
                dp[i][j] = max(left[j],right[j]) + points[i][j]
            prev = dp[i]
            
        return max(dp[m-1])