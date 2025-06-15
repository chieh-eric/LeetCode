from collections import defaultdict
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        direction = {
            1:[(0,-1),(0,1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(1,0),(0,1)],
            5:[(0,-1),(-1,0)],
            6:[(-1,0),(0,1)]
        }

        reverse = {
            (0,1):(0,-1),
            (0,-1):(0,1),
            (1,0):(-1,0),
            (-1,0):(1,0)
        }

        def dfs(i,j):
            if i == m - 1 and j == n - 1:
                return True
            visited[i][j] = True

            for dx, dy in direction[grid[i][j]]:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if reverse[(dx,dy)] in direction[grid[nx][ny]]:
                        if dfs(nx,ny):
                            return True
            return False

        return dfs(0,0)
            