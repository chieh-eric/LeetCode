class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        max_area = -1
        n = len(points)
        points_set = set((val[0],val[1]) for val in points)
        #print(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                
                if x1 == x2 or y1 == y2:
                    continue

                if (x1,y2) in points_set and (x2,y1) in points_set:
                    good = True
                    left = min(x1,x2)
                    right = max(x1,x2)
                    top = max(y1,y2)
                    bottom = min(y1,y2)

                    for x3, y3 in points:
                        if (x3,y3) in [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]:
                            continue
                        if left <= x3 <= right and bottom <= y3 <= top:
                            good = False
                            break
                    
                    if good:
                        max_area = max(max_area,abs(x1-x2)*abs(y1-y2))

                    
        return max_area