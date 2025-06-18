import heapq
class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = {}
        for i, j, cost in connections:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append((cost,j))
            graph[j].append((cost,i))
        
        visited = set()
        queue = []
        visited.add(1)
        for edge in graph[1]:
            heapq.heappush(queue,edge)
        count = 0
        while queue:
            cost, node  =  heapq.heappop(queue)
            
            if node in visited:
                continue

            visited.add(node)
            count += cost
            
            for edge in graph[node]:
                if edge[1] not in visited:
                    heapq.heappush(queue,edge)

        return count if len(visited) == n else -1
     

#  4 <- 3 <- 1 -> 2 
