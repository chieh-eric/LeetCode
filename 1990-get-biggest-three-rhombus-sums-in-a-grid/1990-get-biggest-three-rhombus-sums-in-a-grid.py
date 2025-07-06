import heapq
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        result = set()
        # i, j means center of rhombus
        for i in range(m):
            for j in range(n):
                result.add(grid[i][j])
                min_k = min(i, j, m-i-1, n-j-1)
                for k in range(1,min_k+1):
                    total = 0
                    x, y = i, j
                    for d in range(1,k):
                        total += grid[x+k-d][y-d]
                        total += grid[x+d][y+k-d]
                        total += grid[x-d][y-k+d]
                        total += grid[x-k+d][y+d]
                    total += grid[x+k][y]
                    total += grid[x-k][y]
                    total += grid[x][y+k]
                    total += grid[x][y-k]
                    result.add(total)
        return sorted(result,reverse=True)[:3]




