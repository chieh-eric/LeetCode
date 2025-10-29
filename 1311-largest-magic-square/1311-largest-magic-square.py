class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Appraoch
        # Use prefix sum, sum each row, each col and the diagonal

        # start iterate from the largest length
        # O(n^2)

        n = len(grid)
        m = len(grid[0])
        rows = [[0]*m for _ in range(n)]
        cols = [[0]*m for _ in range(n)]
        diagonals1 = [[0]*m for _ in range(n)]
        diagonals2 = [[0]*m for _ in range(n)]

        for i in range(n):
            cur = 0
            for j in range(m):
                cur += grid[i][j]
                rows[i][j] = cur
        
        #print(rows)

        for j in range(m):
            cur = 0
            for i in range(n):
                cur += grid[i][j]
                cols[i][j] = cur
        
        #print(cols)

        for i in range(n):
            diagonals1[i][0] = grid[i][0]
        for j in range(m):
            diagonals1[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                diagonals1[i][j] = diagonals1[i-1][j-1] + grid[i][j]
        #print(diagonals1)

        for i in range(n):
            diagonals2[i][-1] = grid[i][-1]
        for j in range(m):
            diagonals2[0][j] = grid[0][j]
        
        for i in range(1,n):
            for j in range(m-2,-1,-1):
                diagonals2[i][j] = diagonals2[i-1][j+1] + grid[i][j]
        #print(diagonals2)

        larget_length = min(n, m)
        for length in range(larget_length, 0,-1):
            for i in range(n - length + 1):
                for j in range(m - length + 1):
                    first = True
                    target = 0
                    found = True
                    if first:
                        target = rows[i][j+length-1] - rows[i][j] + grid[i][j]
                        first = False
                    
                    for ii in range(i, i+length):
                        if target != rows[ii][j+length-1] - rows[ii][j] + grid[ii][j]:
                            #if length == 3 and i == 1 and j == 1:
                                # print("fuckdaskdka")
                                # print(target, rows[ii][j+length-1] - rows[ii][j] + grid[ii][j])
                            found = False
                            break
                    for jj in range(j, j+length):
                        if target != cols[i+length-1][jj] - cols[i][jj] + grid[i][jj]:
                            #if length == 3 and i == 1 and j == 1:
                                # print("fuckdaskdka")
                                # print(target, cols[i][jj] - cols[i][jj] + grid[i][jj])
                            found = False
                            break
                    
                    if target != diagonals1[i+length-1][j+length-1] - diagonals1[i][j] + grid[i][j]:
                        found = False
                    
                    if target != diagonals2[i+length-1][j] - diagonals2[i][j+length-1] + grid[i][j+length-1]:
                        found = False

                    if found:
                        return length




