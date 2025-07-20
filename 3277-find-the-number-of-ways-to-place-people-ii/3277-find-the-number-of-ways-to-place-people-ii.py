class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:(x[0],-x[1]))
        n = len(points)
        count = 0
        res = 0

        for i in range(n):
            _, iy = points[i]
            y = -float('inf')
            for j in range(i+1,n):
                if iy >= points[j][1] > y:
                    res += 1
                    y = points[j][1]
        return res