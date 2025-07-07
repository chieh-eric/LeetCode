from collections import defaultdict
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = {}
        boarder = {}
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            if grid[i][j] == 0:
                return 0, set((i,j))
            
            if grid[i][j] == -1:
                return
            
            size = 1
            board = set()
            grid[i][j] = -1
            direction = [(0,1),(1,0),(0,-1),(-1,0)]
            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 0:
                        board.add((nx,ny))
                    elif grid[nx][ny] == 1:
                        s, b = dfs(nx,ny)
                        size += s
                        board.update(b)
            return size, board


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dic[(i,j)], boarder[(i,j)] = dfs(i,j)
                    
        

        boarder_value = defaultdict(int)
        for key in boarder:
            for i, j in boarder[key]:
                boarder_value[(i,j)] += dic[key]

        if not boarder_value:
            if dic:
                return m*n
            else:
                return 1
        return max(boarder_value.values()) + 1
                    
                    
      