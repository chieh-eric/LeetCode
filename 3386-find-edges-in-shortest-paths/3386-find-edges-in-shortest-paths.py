from collections import defaultdict
import heapq
class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        graph = defaultdict(list)
        for index,(i, j, w) in enumerate(edges):
            graph[i].append((j,w,index))
            graph[j].append((i,w,index))

        m = len(edges)
        res = [False]*m
        heap = [(0,0,-1)]
        shortest = float('inf')
        visited = set()
        while heap:
            step, node, i = heapq.heappop(heap)
            if node == n-1:
                shortest = step
                break
            visited.add(node)
            for nei, w, idx in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap,(step+w,nei,idx))

        if shortest == float('inf'):
            return res
        def dfs(node,parent,length):
            if length > shortest:
                return False

            if node == n - 1 and length == shortest:
                return True

            valid = False
            for nei, w, idx in graph[node]:
                if nei == parent:
                    continue
                if(dfs(nei,node,length+w)):
                    res[idx] = True
                    valid = True
            return valid
        dfs(0,None,0)
        return res

