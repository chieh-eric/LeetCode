from collections import defaultdict
import heapq
class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        ans = [-1]*n
        ans[0] = 0
        graph = defaultdict(list)
        for i,j, cost in edges:
            graph[i].append((cost,j))
            graph[j].append((cost,i))
        
        queue = []
        for edge in graph[0]:
            heapq.heappush(queue,edge)
        
        visited = set()
        visited.add(0)

        while queue:
            edge = heapq.heappop(queue)
            if edge[1] in visited:
                continue
            

            if disappear[edge[1]] > edge[0]:
                ans[edge[1]] = edge[0]
                visited.add(edge[1])
                for child in graph[edge[1]]:
                    if child[1] not in visited:
                        heapq.heappush(queue,(child[0]+edge[0],child[1]))
        return ans