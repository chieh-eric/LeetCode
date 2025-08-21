class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        m = len(workers)
        n = len(bikes)
        distance = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                distance[i][j] = abs(bikes[i][0]-workers[j][0]) + abs(bikes[i][1]-workers[j][1])
        #print(distance)

        dp = [float('inf')]*(2**n)
        dp[0] = 0

        for mask in range(2**n):

            i = bin(mask).count("1")
            
            if i >= m:
                continue
            
            for j in range(n):
                if not ((mask >> j) & 1):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + distance[j][i])

        min_val = float('inf')
        for mask in range(2**n):
            if bin(mask).count("1") == m:
                min_val = min(min_val, dp[mask])
        return min_val
        #print(dp)

