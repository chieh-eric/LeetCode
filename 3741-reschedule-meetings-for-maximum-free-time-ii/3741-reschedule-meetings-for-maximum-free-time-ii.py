import heapq
import bisect
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        gap = []
        gap.append(startTime[0])
        for i in range(1,len(startTime)):
            gap.append(startTime[i] - endTime[i-1])
        gap.append(eventTime -  endTime[-1])
        n = len(gap)

        largestLeft = [0]*n
        largestRight = [0]*n
    

        for i in range(1,n):
            largestLeft[i] = max(largestLeft[i-1], gap[i-1])
    
        
        for i in range(n-3,-1,-1):
            largestRight[i] = max(largestRight[i+1],gap[i+2])
        
        maxi = 0
        maxi = max(maxi,max(gap))

        duration = [endTime[i] - startTime[i] for i in range(len(startTime))]
     
        for i in range(len(duration)):
            size = duration[i]
            if largestLeft[i] >= size or largestRight[i] >= size:
                maxi = max(maxi,gap[i]+gap[i+1]+size)
            else:
                maxi = max(maxi,gap[i]+gap[i+1])
        return maxi

        