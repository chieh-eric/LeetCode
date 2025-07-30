class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = set()
        count_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    count_fresh += 1
                    fresh.add((i,j))
        if count_fresh == 0:
            return 0

        cur = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            i, j, time = queue.popleft()

            if time != 0:
                cur.add((i,j))
            if len(cur) == len(fresh):
                return time

            grid[i][j] = 2
            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < m and  0 <= ny < n and grid[nx][ny] == 1:
                    queue.append((nx,ny,time+1))
        
        return -1
          
        