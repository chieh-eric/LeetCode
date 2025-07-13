class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        memo = {}

        def dfs(row,j1,j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2>= m or row >= n:
                return 0
            
            if (row,j1,j2) in memo:
                return memo[(row,j1,j2)]
            
            score = 0
            if j1 == j2:
                score = grid[row][j1]
            else:
                score = grid[row][j1] + grid[row][j2]
            
            max_cherry = 0
            for dj1 in [1,-1,0]:
                for dj2 in [1,-1,0]:
                    max_cherry = max(max_cherry,dfs(row+1,j1+dj1,j2+dj2))
            result = max_cherry + score
            memo[(row,j1,j2)] = result
            return result
        return dfs(0,0,m-1)

                    