import heapq
from collections import defaultdict
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        heap = []
        n = len(grid)
        m = len(grid[0])

        graph = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    graph[(i,j)].append((1,i+1,j))
                    graph[(i,j)].append((0,i,j+1))
                    graph[(i,j)].append((1,i-1,j))
                    graph[(i,j)].append((1,i,j-1))
                elif grid[i][j] == 2:
                    graph[(i,j)].append((1,i+1,j))
                    graph[(i,j)].append((1,i,j+1))
                    graph[(i,j)].append((1,i-1,j))
                    graph[(i,j)].append((0,i,j-1))
                elif grid[i][j] == 3:
                    graph[(i,j)].append((0,i+1,j))
                    graph[(i,j)].append((1,i,j+1))
                    graph[(i,j)].append((1,i-1,j))
                    graph[(i,j)].append((1,i,j-1))
                else:
                    graph[(i,j)].append((1,i+1,j))
                    graph[(i,j)].append((1,i,j+1))
                    graph[(i,j)].append((0,i-1,j))
                    graph[(i,j)].append((1,i,j-1))

        heapq.heappush(heap,(0,0,0))
        
        min_cost = float('inf')
        visited = [[False]*m for _ in range(n)]
        while heapq:
            #print(heap)
            cost, x, y = heapq.heappop(heap)
            
            if x == n - 1 and y == m - 1:
                return cost 

            if visited[x][y]:
                continue
            
            visited[x][y] = True
        
            for c, dx, dy in graph[(x,y)]:
                if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
                    heapq.heappush(heap,(cost+c,dx,dy))