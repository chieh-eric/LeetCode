class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numSquare = 1
        n = len(grid)
        m = len(grid[0])
        start_i = start_j = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    numSquare += 1
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
        
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        self.routes = 0
        def dfs(i,j,countSquare,path):
            if grid[i][j] == 2:
                #print(countSquare)
                if countSquare == numSquare:
                    self.routes += 1
                return
            #print((i,j))
            path.add((i,j))
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx,ny) not in path and grid[nx][ny] != -1 and grid[nx][ny] != 1:
                        dfs(nx, ny, countSquare + 1, path.copy())
        
        dfs(start_i, start_j, 0, set())
        return self.routes
                        

            