class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        gaps = numRows - 2
        n = len(s)
        if numRows == 1:
            return s
        if numRows == 2:
            s = s[0:n:2] + s[1:n:2]
            return s
        print(n)
        col = (n//(numRows+gaps)*(gaps+1)) + ((n%(numRows+gaps)+(numRows-1)) // numRows) + max((n%(numRows+gaps)- numRows),0)
       # print(col)
        table = [[""]*col for _ in range(numRows)]
        
        cur_row = 0
        cur_col = 0
        start = True
        i = 0
        while i < n:
            if cur_row == numRows:
                cur_row -=  2
                cur_col += 1
                while i < n and cur_row != 0:
                    table[cur_row][cur_col] = s[i]
                    cur_row -= 1
                    cur_col += 1
                    i += 1
            else:
                table[cur_row][cur_col] = s[i]
                cur_row += 1
                i += 1
        #print(table)
        res = ""
        for i in range(numRows):
            for j in range(col):
                if table[i][j] != "":
                    res += table[i][j]
        return res