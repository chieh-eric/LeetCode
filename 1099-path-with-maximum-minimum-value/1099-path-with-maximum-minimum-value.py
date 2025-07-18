import heapq
class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_val = float('inf')
        heap = []
        heapq.heappush(heap,((-grid[0][0],(0,0))))
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        m = len(grid[0])
        visited = set()

        while heap:
            neg_val, (x,y) = heapq.heappop(heap)
            min_val = min(min_val,-neg_val)
            
            if (x,y) in visited:
                continue
            
            visited.add((x,y))
            if x == n - 1 and y == m - 1:
                return min_val
            
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited:
                    heapq.heappush(heap,(-grid[nx][ny],(nx,ny)))
        
        return min_val