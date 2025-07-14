class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        visited = set()
        queue = deque()
        queue.append((0,0,k,0))
        m = len(grid)
        n = len(grid[0])

        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            x, y, remain, step = queue.popleft()
            
            if x == m - 1 and y == n - 1:
                return step

            if grid[x][y] == 1:
                remain -= 1

            if (x,y,remain) in visited:
                continue
                
            visited.add((x,y,remain))
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny,remain) not in visited and remain >= 0:
                    queue.append((nx,ny,remain,step+1))
        return -1