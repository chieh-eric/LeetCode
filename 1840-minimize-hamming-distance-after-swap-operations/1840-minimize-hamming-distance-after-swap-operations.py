from collections import defaultdict
class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
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

        for i, j in  allowedSwaps:
            union(i,j)
        
        n = len(source)
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        #print(groups)
        count = 0
        for key in groups:
            group = groups[key]
            value = defaultdict(int)
            for idx in group:
                value[source[idx]] += 1

            for index in group:
                if target[index] in value and value[target[index]] > 0:
                    value[target[index]] -= 1
                else:
                    count += 1
        return count
