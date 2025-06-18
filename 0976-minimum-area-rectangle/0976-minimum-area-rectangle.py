class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:(x[0],x[1]))
        set_points = set()
        for point in points:
            set_points.add((point[0],point[1]))
        min_val = float('inf')
        for x, y in points:
            for nx, ny in points:
                if x != nx and y != ny:
                    if (x,ny) in set_points and (nx,y) in set_points:
                        min_val = min(min_val,abs(x-nx)*abs(y-ny))
        return min_val if min_val != float('inf') else 0