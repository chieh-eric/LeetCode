import heapq
class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
            return

        if num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        self.rebalance()

    def rebalance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            popValue = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -popValue)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            popValue = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -popValue)
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / float(2)
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()