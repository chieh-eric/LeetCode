class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        matrix = [[1]*n for _ in range(n)]
        rows = [[0]*n for _ in range(n)]
        cols = [[0]*n for _ in range(n)]
        for i, j in mines:
            matrix[i][j] = 0
        
        
        for i in range(n):
            row = 0
            for j in range(n):
                row += matrix[i][j]
                rows[i][j] = row 

        for j in range(n):
            col = 0
            for i in range(n):
                col += matrix[i][j]
                cols[i][j] = col
        # print(matrix)
        # print(rows)
        # print(cols)

        max_order = n // 2 if n % 2 else n // 2 - 1

        for order in range(max_order,0, -1):
            for i in range(order, n - order):
                for j in range(order, n - order):
                    if rows[i][j+order] - rows[i][j-order] + matrix[i][j-order] == 2*order + 1 and cols[i+order][j] - cols[i-order][j] + matrix[i-order][j] == 2*order + 1:
                        return order + 1
        return 1 if len(mines) != n*n else 0

        