class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        res = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [0]*i
            temp[0] = temp[-1] = 1
            for j in range(1,i-1):
                temp[j] = res[-1][j-1] + res[-1][j]
            res.append(temp)
        return res