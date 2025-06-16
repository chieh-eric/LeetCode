class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        count = 0
       
        if startPos[0] < homePos[0]:
            for i in range(startPos[0]+1,homePos[0]+1):
                count += rowCosts[i]
        elif startPos[0] > homePos[0]:
            for i in range(startPos[0]-1,homePos[0]-1,-1):
                count += rowCosts[i]
        
        if startPos[1] < homePos[1]:
            for i in range(startPos[1]+1,homePos[1]+1):
                count += colCosts[i]
        elif startPos[1] > homePos[1]:
            for i in range(startPos[1]-1,homePos[1]-1,-1):
                count += colCosts[i]
        
        return count