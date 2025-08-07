class RangeModule(object):

    def __init__(self):
        self.track = SortedDict()
        

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        
        drop = []
        start, end = left, right

        for s, e in self.track.items():
            if e < start:
                continue
            
            if s > end:
                continue
            
            start = min(start, s)
            end = max(end, e)
            
            drop.append(s)

        while drop:
            del self.track[drop.pop()]

        self.track[start] = end
        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        idx = self.track.bisect_right(left) - 1
        if idx < 0 or self.track.peekitem(idx)[1] < right:
            return False
        return True
        
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        drop = []
        start, end = left, right

        for s, e in self.track.items():
            if e < start:
                continue
            
            if s > end:
                continue
            
            start = min(start, s)
            end = max(end, e)
            
            drop.append(s)

        while drop:
            del self.track[drop.pop()]

        if start < left:
            self.track[start] = left
        
        if end > right:
            self.track[right] = end
        
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)