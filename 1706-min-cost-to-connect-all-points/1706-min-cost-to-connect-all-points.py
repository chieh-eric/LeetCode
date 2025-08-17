from collections import defaultdict
import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        def distance(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        heap = []
        heapq.heappush(heap,(0,0))
        visited = set()
        total = 0

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            
            total += cost
            visited.add(node)
            if len(visited) == n:
                return total

            px = points[node][0]
            py = points[node][1]

            for index, (x,y) in enumerate(points):
                if node == index:
                    continue
                if index not in visited:
                    heapq.heappush(heap,(distance((x,y),(px,py)), index))