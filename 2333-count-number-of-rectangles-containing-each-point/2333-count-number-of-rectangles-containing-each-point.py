import bisect
from collections import defaultdict
class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        height_map = defaultdict(list)
        for x, y in rectangles:
            height_map[y].append(x)
        
        for key in height_map:
            height_map[key].sort()
        
        res = []
        for point in points:
            i = point[0]
            j = point[1]
            count = 0
            for k in range(j,101):
                if k in height_map:
                    n = len(height_map[k])
                    idx = bisect.bisect_left(height_map[k],i)
                    count += (n-idx)
            res.append(count)
        return res

