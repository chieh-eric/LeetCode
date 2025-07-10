import heapq
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n = len(apples)
        heap = []
        eat = 0
        day = 0

        while day < n or heap:
            if day < n and apples[day] > 0:
                heapq.heappush(heap,(day+days[day],apples[day]))
            
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            
            if heap:
                expire, count = heapq.heappop(heap)
                eat += 1
                if count > 1:
                    heapq.heappush(heap,(expire,count-1))
            day += 1
        return eat
        

        