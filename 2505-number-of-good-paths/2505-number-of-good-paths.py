from collections import defaultdict
class UnionFind():
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        nx = self.find(x)
        ny = self.find(y)
        if nx != ny:
            self.parent[nx] = ny

class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(vals)
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        vals_to_node = defaultdict(list)
        for i, val in enumerate(vals):
            vals_to_node[val].append(i)
        
        u = UnionFind(n) 
        total = 0
        for val in sorted(vals_to_node):
            for node in vals_to_node[val]:
                for nei in graph[node]:
                    if val >= vals[nei]:
                        u.union(node,nei)
            
            group_count = defaultdict(int)
            for node in vals_to_node[val]:
                root = u.find(node)
                group_count[root] += 1
            
            for count in group_count.values():
                total += count*(count+1) // 2
        return total
        