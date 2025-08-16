from collections import defaultdict
import heapq
class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        heap = []
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,-w))

        heapq.heappush(heap,(0,0,0))

        visited = set()
        while heap:
            cost, node, used = heapq.heappop(heap)
            if node == n - 1:
                return cost
            if ((node,used)) in visited:
                continue
                
            visited.add((node,used))
            for nei, wei in graph[node]:
                if nei not in visited:
                    if wei < 0:
                        heapq.heappush(heap,(2*(-wei)+cost,nei,1))
                    else:
                        heapq.heappush(heap,(wei+cost,nei,0))
        return -1