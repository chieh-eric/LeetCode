import heapq
from collections import Counter
class FreqStack(object):

    def __init__(self):
        self.heap = []
        self.idx = 0
        self.count = Counter()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.count[val] += 1
        heapq.heappush(self.heap,(-self.count[val],-self.idx,val))
        self.idx += 1

        

    def pop(self):
        """
        :rtype: int
        """
        val = heapq.heappop(self.heap)[2]
        self.count[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()