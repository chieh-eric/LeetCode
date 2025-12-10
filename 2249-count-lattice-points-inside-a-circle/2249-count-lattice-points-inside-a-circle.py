class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        point = set()
        for x, y, r in circles:
            for x1 in range(x - r, x+r+1):
                for y1 in range(y-r, y+r+1):
                    if (x1-x)**2 + (y1-y)**2 <= r**2:
                        point.add((x1,y1))
        return len(point)