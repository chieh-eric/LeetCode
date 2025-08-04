class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        base = grid[0]
        n = len(grid)
        m = len(grid[0])
        for i in range(1,n):
            if base == grid[i]:
                continue
            for j in range(m):
                if base[j] == grid[i][j]:
                    return False
        return True
            