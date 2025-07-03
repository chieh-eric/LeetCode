from collections import defaultdict
import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        visited = [False]*n
        heap = [(0,0)]
       
        total_weight = 0
        count = 0
        while heap and count < n:
            weight, node = heapq.heappop(heap)
            if visited[node]:
                continue
                
            total_weight += weight
            count += 1
            visited[node] = True
            
            x = points[node][0]
            y = points[node][1]
            for adj_node, (x1, y1) in enumerate(points):
                if adj_node != node and not visited[adj_node]:
                    adj_weight = abs(x1-x) + abs(y1 - y)
                    heapq.heappush(heap,(adj_weight,adj_node))
        return total_weight

