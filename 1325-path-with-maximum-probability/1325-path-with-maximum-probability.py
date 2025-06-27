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
        visited = [False]*n

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob

            if node == end_node:
                return prob

            if visited[node]:
                continue

            visited[node] = True

            for route_prob, neighbor in graph[node]:
                if not visited[neighbor]:
                    new_prob = prob * route_prob
                    heapq.heappush(heap,(-new_prob,neighbor))
        return 0
        