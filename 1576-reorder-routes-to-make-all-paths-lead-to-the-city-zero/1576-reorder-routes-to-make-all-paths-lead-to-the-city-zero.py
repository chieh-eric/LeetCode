from collections import defaultdict
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        edges = set()
        def dfs(node,parent):
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                edges.add((nei,node))
                dfs(nei,node)
        dfs(0,None)
        #print(edges)
        orig = set()
        for item in connections:
            orig.add((item[0],item[1]))

        return len(edges - orig)