import heapq
class MinStack(object):

    def __init__(self):
        self.heap = []
        self.stack = []
        self.exist = Counter()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        heapq.heappush(self.heap,val)
        self.exist[val] += 1

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        self.exist[val] -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        while self.heap:
            val = self.heap[0]
            if self.exist[val] > 0:
                return val
            else:
                heapq.heappop(self.heap)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()