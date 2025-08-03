class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        left = [[0]*n for _ in range(m)]
        for i in range(m):
            left[i][0] = grid[i][0]

        down =  [[0]*n for _ in range(m)]
        for i in range(n):
            down[0][i] = grid[0][i]

        for j in range(n):
            for i in range(1,m):
                down[i][j] += down[i-1][j] + grid[i][j]
        

        for i in range(m):
            for j in range(1,n):
                left[i][j] += left[i][j-1] + grid[i][j]

       
        for length in range(min(m,n), 0, -1):
            for i in range(m-length+1):
                for j in range(n-length+1):
                    if grid[i][j] != 1 or grid[i+length-1][j] != 1 or grid[i+length-1][j+length-1] != 1 or grid[i][j+length-1] != 1:
                        continue
                   
                    if left[i][j+length-1] - left[i][j] == length - 1:
                        if left[i+length-1][j+length-1] - left[i+length-1][j] == length - 1:
                            if down[i+length-1][j] - down[i][j] == length - 1:
                                if down[i+length-1][j+length-1] - down[i][j+length-1] == length - 1:
                                    return length**2
        return 0
# 1 1 0
# 1 1 1
# 1 1 1
# 0 1 0
# 1 1 1
# 0 1 1
# 1 1 1
        
# 1 2 3
# 1 1 2
# 1 2 3

# 1 1 1
# 2 1 2
# 3 2 3


# 1 2 2
# 1 2 3
# 1 2 3
# 1 2 3


# 1 1 0
# 2 2 1
# 3 3 2
# 4 4 3