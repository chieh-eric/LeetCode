class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i, j)]

            if i == rows:
                return j

            if grid[i][j] == 1:
                if j + 1 >= cols or grid[i][j + 1] == -1:
                    return -1
                ret = dfs(i + 1, j + 1)
                if ret == -1:
                    dp[(i, j)] = -1
                else:
                    dp[(i, j)] = ret
                return dp[(i, j)]
                
            if grid[i][j] == -1:
                if j -1 < 0 or grid[i][j - 1] == 1:
                    return -1
                ret = dfs(i + 1, j - 1)
                if ret == -1:
                    dp[(i, j)] = -1
                else:
                    dp[(i, j)] = ret
                
                return dp[(i, j)]


        
        ans = []
        for i in range(cols):
            ans.append(dfs(0, i))
        return ans
            
            

        