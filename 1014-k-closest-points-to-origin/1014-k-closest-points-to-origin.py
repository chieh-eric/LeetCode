import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calculate(x,y):
            return x*x + y*y
        heap = []
        for x, y in points:
            heapq.heappush(heap,(calculate(x,y),x,y))
        res = []
        while heap and k > 0:
            _, x, y = heapq.heappop(heap)
            res.append((x,y))
            k -= 1
        return res
