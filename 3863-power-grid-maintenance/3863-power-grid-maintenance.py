from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x, y):
        px = self.find(x)
        py = self.find(y)

        self.parent[px] = py

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        uf = UnionFind(c+1)
        #graph = defaultdict(list)
        for i, j in connections:
            uf.union(i, j)
            # graph[i].append(j)
            # graph[j].append(i)
                
        for i in range(1,c+1):
            uf.find(i)
        group = defaultdict(SortedList)
        for i in range(1, c+1):
            group[uf.parent[i]].add(i)
        #print(group)

        for t, node in queries:

            idx = group[uf.parent[node]].bisect_left(node)
            #print(idx)
            if t == 1:
                if not group[uf.parent[node]]:
                    ans.append(-1)
                else:
                    if idx < len(group[uf.parent[node]]) and group[uf.parent[node]][idx] == node:
                        ans.append(node)
                    else:
                        ans.append(group[uf.parent[node]][0])
            else:
                group[uf.parent[node]].discard(node)
        return ans