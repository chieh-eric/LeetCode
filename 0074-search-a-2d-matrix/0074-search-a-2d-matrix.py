class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        n = len(matrix)
        m = len(matrix[0])

        up = 0
        down = n - 1

        while up < down:
            mid = (up+down+1) // 2
            val = matrix[mid][0]
            
            if val > target:
                down = mid - 1
            else:
                up = mid
        #print(up)

        left = 0
        right = m - 1

        while left <= right:
            mid = (left+right) // 2
            val = matrix[up][mid]
            #print(val)
            if val == target:
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False