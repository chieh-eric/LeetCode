from collections import defaultdict
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        visited = [False]*n
        for f, e in edges:
            graph[f].append(e)
            graph[e].append(f)
        

        count = 0
        def group(i):
            visited[i] = True
            nodes = 1
            contain = [i]
            for nei in graph[i]:
                if not visited[nei]:
                    node , sub = group(nei)
                    nodes += node
                    contain += sub
            return nodes, contain

        
        for i in range(n):
            if not visited[i]:
                node_count, groups = group(i)
                valid = True
                for node in groups:
                    if len(graph[node]) != node_count - 1:
                        valid = False
                        break
                if valid:
                    count += 1
        return count            
                    
