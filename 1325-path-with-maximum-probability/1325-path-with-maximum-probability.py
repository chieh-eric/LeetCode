from collections import defaultdict
import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for index,(i, j) in enumerate(edges):
            graph[i].append((succProb[index], j))
            graph[j].append((succProb[index], i))
        
        heap = []
        heapq.heappush(heap,(-1,start_node))
        visited = set()

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob

            if node == end_node:
                return prob

            if node in visited:
                continue

            visited.add(node)

            for route_prob, neighbor in graph[node]:
                if neighbor not in visited:
                    new_prob = prob * route_prob
                    heapq.heappush(heap,(-new_prob,neighbor))
        return 0
        