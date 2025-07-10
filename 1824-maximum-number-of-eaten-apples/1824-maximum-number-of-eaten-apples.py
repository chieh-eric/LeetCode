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


        for i in range(n):
            heapq.heappush(heap,(i+days[i],apples[i]))
            
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            #print(heap)
            if heap:
                day, count = heapq.heappop(heap)
                if day > i:
                    eat += 1
                    count -= 1
                if count == 0 or day <= i:
                    continue
                heapq.heappush(heap,(day,count))
       #print(eat)
        #print("start")
        cur_day = n 
        while heap:
            while heap and heap[0][0] <= cur_day:
                heapq.heappop(heap)
            #print(heap)
            if heap:
                day, count = heapq.heappop(heap)
                if day > cur_day:
                    eat += 1
                    count -= 1
                if count != 0 and day > cur_day:
                    heapq.heappush(heap,(day,count))
            cur_day += 1
            #print("cur")
            #print(cur_day)
        return eat

        