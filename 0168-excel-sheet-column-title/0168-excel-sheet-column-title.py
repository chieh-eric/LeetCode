class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        
        while columnNumber > 0:
            remain = columnNumber % 26
            columnNumber = columnNumber // 26
            if remain != 0:
               res = chr(ord('A')-1+ remain) + res
            else:
                columnNumber -=1
                res = "Z"+res
                
            #print(res)
        return res