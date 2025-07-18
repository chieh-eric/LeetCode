import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key= lambda x:(x[0],x[1]))
        #print(events)
        heap = []
        attend = 0
        n = len(events)
        
        index = 0
        day = 0
        while heap or index < n:
            if not heap:
                day = events[index][0]

            while index < n and events[index][0] == day:
                heapq.heappush(heap,events[index][1])
                index += 1
            
            while heap and day > heap[0]:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                attend += 1
            day += 1
        return attend

