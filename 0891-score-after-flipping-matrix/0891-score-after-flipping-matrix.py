class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = grid[i][j] ^ 1
        
        for j in range(1,m):
            count = 0
            for i in range(n):
                count += grid[i][j]
            if count <= n/2:
                for i in range(n):
                    grid[i][j] = grid[i][j] ^ 1
        ret = 0
        for i in range(n):
            res = []
            for j in range(m):
                res.append(str(grid[i][j]))
            
            num = int(''.join(res),2)
            ret += num
        return ret