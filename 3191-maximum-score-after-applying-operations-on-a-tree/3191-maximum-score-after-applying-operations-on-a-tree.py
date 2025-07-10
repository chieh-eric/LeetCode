from collections import defaultdict
class Solution(object):
    def maximumScoreAfterOperations(self, edges, values):
        """
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        total = sum(values)
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(parent,node):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return values[node]
            
            child_cost = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_cost += dfs(node,child)
            
            return min(child_cost,values[node])
        
        min_val = dfs(None,0)
        return total - min_val