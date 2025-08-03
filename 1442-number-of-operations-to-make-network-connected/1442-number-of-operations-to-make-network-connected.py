class UnionFind():
    def __init__(self,n):
        self.parent = [val for val in range(n)]
    
    def find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self,a,b):
        na = self.find(a)
        nb = self.find(b)
        
        self.parent[na] = nb

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        u = UnionFind(n)
        edges = 0
        for i, j in connections:
          
            ni = u.find(i)
            nj = u.find(j)
            if ni != nj:
                u.union(ni,nj)
            else:
                edges += 1
        
        not_connnect = set()
        for i in range(n):
            not_connnect.add(u.find(i))
        
        if len(not_connnect) - 1 > edges:
            return -1
        return len(not_connnect) - 1
        