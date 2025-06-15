class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        row = [[0] *m for _ in range(n)]
        col = [[0] *m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i][j] = (row[i][j-1] if j > 0 else 0) + 1
                    col[i][j] = (col[i-1][j] if i > 0 else 0) + 1
        
       
        for length in range(min(n, m),0,-1):
            for i in range(n-length+1):
                for j in range(m-length+1):
                    x = i + length - 1
                    y = j + length - 1
                    if (row[i][y] >= length and
                        row[x][y] >= length and
                        col[x][j] >= length and
                        col[x][y] >= length):
                        return length * length
        return 0


# 1 2 2
# 1 2 3
# 1 2 3
# 1 2 3


# 1 1 0
# 2 2 1
# 3 3 2
# 4 4 3