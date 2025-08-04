class DetectSquares(object):

    def __init__(self):
        self.counts = Counter()
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.counts[tuple(point)] += 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        #print(self.counts)
        x2, y2 = point
        total = 0
        for key in self.counts:
            x1, y1 = key
            dia = self.counts[key]
            if x1 != x2 and y1 != y2 and (abs(x1-x2) == abs(y1-y2)):
                if (x1,y2) in self.counts and (x2,y1) in self.counts:
                    total += dia*(self.counts[(x1,y2)])*(self.counts[(x2,y1)])
        return total



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)