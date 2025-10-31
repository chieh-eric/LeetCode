class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i == rows:
                return j

            if grid[i][j] == 1:
                if j + 1 >= cols or grid[i][j + 1] == -1:
                    return -1
                return dfs(i + 1, j + 1)
            if grid[i][j] == -1:
                if j -1 < 0 or grid[i][j - 1] == 1:
                    return -1
                return dfs(i + 1, j - 1)
        
        ans = []
        for i in range(cols):
            ans.append(dfs(0, i))
        return ans
            
            

        