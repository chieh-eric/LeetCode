from collections import defaultdict
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x1 = find(x)
            y1 = find(y)
            parent[x1] = y1
        
        for i, j in pairs:
            union(i,j)
        
        group = defaultdict(list)
        
        for index in parent:
            root = find(index)
            group[root].append(index)

        res = list(s)
        for key in group:
            indicies = sorted(group[key])
            values = [s[i] for i in indicies]
            values.sort()

            for i, idx in enumerate(indicies):
               
                res[idx] = values[i]
        return "".join(res)