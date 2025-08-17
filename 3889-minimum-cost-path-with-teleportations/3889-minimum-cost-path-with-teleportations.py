from collections import defaultdict
import heapq
class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[[False]*(k+1) for _ in range(n)]for _ in range(m)]
        teleport = defaultdict(list)
        vals = []
        for i in range(m):
            for j in range(n):
                vals.append((grid[i][j],i,j))
        vals.sort()

        for index, (val, i, j) in enumerate(vals):
            idx = bisect.bisect_right(vals,(val,float('inf'),float('inf'))) - 1
            for x in range(idx+1):
                if (vals[x][1],vals[x][2]) == (i,j):
                    continue
                teleport[(i,j)].append((vals[x][1],vals[x][2]))
                
        #print(vals)
        #print(teleport)
        direction = [(0,1),(1,0)]
        heap = []
        heapq.heappush(heap,(0,0,0, k))
        while heap:
            cost, i, j, remain = heapq.heappop(heap)
            if visited[i][j][remain]:
                continue
            if i == m - 1 and j == n - 1:
                return cost
            visited[i][j][remain] = True
            for nx, ny in teleport[(i,j)]:
                if not visited[nx][ny][remain] and remain > 0:
                    heapq.heappush(heap,(cost,nx,ny,remain-1))

            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if nx < m and ny < n and not visited[nx][ny][remain]:
                    heapq.heappush(heap,(cost+grid[nx][ny],nx,ny,remain))
      
                    