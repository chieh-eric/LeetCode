import heapq
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        heapq.heappush(queue,(grid[0][0],0,0))
        m = len(grid)
        n = len(grid[0])
        direction = [(0,1),(1,0)]
        visited = set()
        while queue:
            val, i, j = heapq.heappop(queue)
            if i == m - 1 and j == n - 1:
                return val
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                    heapq.heappush(queue,(val+grid[nx][ny],nx,ny))