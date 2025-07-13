import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        n = len(heights)
        jump = []
        count_brick = 0
        for i in range(1,n):
            if heights[i] > heights[i-1]:
                heapq.heappush(jump,heights[i]-heights[i-1])
                if len(jump) > ladders:
                    count_brick += heapq.heappop(jump)
                    if count_brick > bricks:
                        return i - 1
        return n - 1


      