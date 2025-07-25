import heapq
from collections import defaultdict
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = set()
        queue = []
        heapq.heappush(queue,(0,n))
        distance = [0]*(n+1)
        mod = 10**9 + 7
        
        graph = defaultdict(list)
        for i,j, w in edges:
            graph[i].append((j,w))
            graph[j].append((i,w))

        while queue:
            step, node = heapq.heappop(queue)
            if node in visited:
                continue

            visited.add(node)
            distance[node] = step
            if len(visited) == n:
                break
            for nei_node, wei in graph[node]:
                if nei_node not in visited:
                    heapq.heappush(queue,(step+wei,nei_node))
        #print(distance)

        count = 0 
        memo = {}
        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]

            count = 0
            for nei, _ in graph[node]:
                if distance[node] > distance[nei]:
                    count += dfs(nei)
                    count %= mod
            memo[node] = count

            return count

        return dfs(1) % mod
            
        # 6 - 2 - 1 - 3 - 4 - 6
        #      5
        #
        # 