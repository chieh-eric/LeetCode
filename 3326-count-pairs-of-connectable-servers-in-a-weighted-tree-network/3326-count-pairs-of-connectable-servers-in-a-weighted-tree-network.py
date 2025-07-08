from collections import defaultdict
class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        graph = defaultdict(list)

        for i, j, weight in edges:
            graph[i].append((j,weight))
            graph[j].append((i,weight))
            
        n = len(graph)
        res = [0]*n

        def dfs(parent,node,weight):
            count = 0 
            if weight % signalSpeed == 0:
                count += 1
            
            for nei, wei in graph[node]:
                if nei == parent:
                    continue
                count += dfs(node,nei,weight+wei)
            return count
        for node in range(n):
            subtree_count = []
            for nei,w in graph[node]:
                count = dfs(node,nei,w)
                subtree_count.append(count)
            #print(subtree_count)
            
            num = 0
            l = len(subtree_count)
            for i in range(l):
                for j in range(i+1,l):
                    num += subtree_count[i]*subtree_count[j]
            res[node] = num
        return res
        
