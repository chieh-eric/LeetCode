from collections import defaultdict
import heapq
class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.nodes = n
        self.graph = defaultdict(list)
        for fr, to, cost in edges:
            self.graph[fr].append((cost,to))
        

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        self.graph[edge[0]].append((edge[2],edge[1]))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        if node1 == node2:
            return 0
        queue = []
        for edge in self.graph[node1]:
            heapq.heappush(queue,edge)
        
        visited = set()
        visited.add(node1)
        cost = 0
       
        while queue:
            edge = heapq.heappop(queue)
            cost = edge[0]
            to = edge[1]
            if to == node2:
                return cost

            visited.add(to)
            for edge in self.graph[to]:
                if edge[1] not in visited:
                    
                    heapq.heappush(queue,(cost+edge[0],edge[1]))
      
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)