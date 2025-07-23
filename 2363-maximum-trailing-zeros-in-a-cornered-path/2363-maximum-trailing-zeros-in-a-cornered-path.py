class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        # (#of 2, #of 5)
        left = [[(0,0)]*m for _ in range(n)]
        right = [[(0,0)]*m for _ in range(n)]
        up = [[(0,0)]*m for _ in range(n)]
        down = [[(0,0)]*m for _ in range(n)]
        value = [[(0,0)]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                target = grid[i][j]
                count_2 = count_5 = 0
                while target % 2 == 0:
                    count_2 += 1
                    target //= 2

                while target % 5 == 0:
                    count_5 += 1
                    target //= 5
                value[i][j] = (count_2,count_5)
    
        for i in range(n):
            for j in range(1,m):
                count_2, count_5 = value[i][j-1]

                prev_2, prev_5 = left[i][j-1]
                left[i][j] = (prev_2+count_2, prev_5 + count_5)
            
            for j in range(m-2,-1,-1):
                count_2, count_5 = value[i][j+1]


                prev_2, prev_5 = right[i][j+1]
                right[i][j] = (prev_2+count_2, prev_5 + count_5)
        
        for i in range(m):
            for j in range(1,n):
                count_2, count_5 = value[j-1][i]
              

                prev_2, prev_5 = up[j-1][i]
                up[j][i] = (prev_2+count_2, prev_5 + count_5)
            
            for j in range(n-2,-1,-1):
                count_2, count_5 = value[j+1][i]
                prev_2, prev_5 = down[j+1][i]
                down[j][i] = (prev_2+count_2, prev_5 + count_5)
        
     
        max_len = 0
        for i in range(n):
            for j in range(m):
                cur_2, cur_5 = value[i][j]
                max_len = max(max_len, min(sum(value) for value in zip(left[i][j],up[i][j], (cur_2,cur_5))))
                max_len = max(max_len, min(sum(value) for value in zip(left[i][j],down[i][j], (cur_2,cur_5))))
                max_len = max(max_len, min(sum(value) for value in zip(right[i][j],up[i][j], (cur_2,cur_5))))
                max_len = max(max_len, min(sum(value) for value in zip(right[i][j],down[i][j], (cur_2,cur_5))))
        return max_len