import math
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points_set = set()
        for item in points:
            points_set.add((item[0],item[1]))

        n = len(points)
        min_area = float('inf')
        #print(points_set)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]

                    v1 = (p2[0]-p1[0],p2[1]-p1[1])
                    v2 = (p3[0]-p1[0],p3[1]-p1[1])

                    if v1[0]*v2[0] + v1[1]*v2[1] != 0:
                        continue
                    
                    x4 = p2[0]+p3[0]-p1[0]
                    y4 = p2[1]+p3[1]-p1[1]

                    if (x4,y4) in points_set:
                        min_area = min(min_area,math.hypot(v1[0],v1[1])*math.hypot(v2[0],v2[1]))

        return min_area if min_area != float('inf') else 0

            
                    
                