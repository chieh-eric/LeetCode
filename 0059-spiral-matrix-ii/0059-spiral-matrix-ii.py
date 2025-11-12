class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None]*n for _ in range(n)]
        cur = 1
        i = j = 0
        upper_bound = 0
        bottom_bound = n 
        right_bound = n 
        left_bound = 0
        
        while right_bound > left_bound and upper_bound < bottom_bound:
            i = upper_bound
            j = left_bound
            # Horizontal from left to right
            while j < right_bound :
                if matrix[i][j] == None:
                    matrix[i][j] = cur
                    cur += 1
                j += 1
            right_bound -= 1
            # Vertical from top to down
            j -= 1
            while i < bottom_bound:
                if matrix[i][j] == None:
                    matrix[i][j] = cur
                    cur += 1
                i += 1
            bottom_bound -= 1
            # Horizontal from right to left
            i -= 1
            while j >= left_bound:
                if matrix[i][j] == None:
                    matrix[i][j] = cur
                    cur += 1
                j -= 1
            left_bound += 1
            # Vertical from down to top
            j += 1
            while i >= upper_bound:
                if matrix[i][j] == None:
                    matrix[i][j] = cur
                    cur += 1
                i -= 1
            i += 1
            upper_bound += 1
            #print(upper_bound,bottom_bound,right_bound,left_bound)
        #print(matrix)
        return matrix
    # [1,2,3,4],
    # [12,16,13,5],
    # [11,15,14,6],
    # [10,9,8,7]]
