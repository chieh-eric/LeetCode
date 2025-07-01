class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        m = len(grid)
        n = len(grid[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j,length,prev_i,prev_j):
         
            if (i,j) in visited:
                return True

            visited.add((i,j))
            val = grid[i][j]
            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < m and 0 <= ny < n and val == grid[nx][ny] and (nx != prev_i or ny != prev_j):
                    if dfs(nx,ny,length+1,i,j):
                        return True
            return False 
            
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if dfs(i,j,1,None,None):
                        return True
        return False

        # c a d
        # a a a
        # a a d
        # a c d
        # a b c