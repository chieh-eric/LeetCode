from collections import defaultdict
class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for i, j, w in roads:
            graph[i].append((w,j))
            graph[j].append((w,i))
        

        def run(remain):
            arr = list(remain)
            m = len(arr)
            idx = {node:i for i, node in enumerate(arr)}
            dist = [[float('inf')]*m for _ in range(m)]
            for u in arr:
                for w, v in graph[u]:
                    if v in remain:
                        i = idx[u]
                        j = idx[v]
                        dist[i][j] =  min(dist[i][j],w)

            for i in range(m):
                dist[i][i] = 0
            
            for k in range(m):
                for i in range(m):
                    for j in range(m):
                         dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            for i in range(m-1):
                for j in range(i+1,m):
                    if dist[i][j] > maxDistance:
                        return False
            return True


        res = 0
        for i in range(2**n):
            remain = set()
            index = 0
            while i > 0:
                if i & 1:
                    remain.add(index)
                index += 1
                i >>= 1
            if not remain or run(remain):
                res += 1
        return res
            
            # 1 0 (7)
            #   2 (18)