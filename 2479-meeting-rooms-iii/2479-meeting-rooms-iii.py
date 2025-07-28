import heapq
from collections import defaultdict
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        m = len(meetings)
        meetings.sort()
        events = []
        free = []
        count = defaultdict(int)
        for i in range(n):
            heapq.heappush(free,i)

        curTime = 0
        for start, end in meetings:
            curTime = max(curTime,start)
            while events and events[0][0] <= curTime:
                    _, room_id = heapq.heappop(events)
                    heapq.heappush(free,room_id)
            duration = end - start
            if len(free) == 0:
                curTime = events[0][0]
                while events and events[0][0] <= curTime:
                    _, room_id = heapq.heappop(events)
                    heapq.heappush(free,room_id)

            room_id = heapq.heappop(free)
            count[room_id] += 1
            heapq.heappush(events,(curTime + duration,room_id))
        max_key = max(count,key=count.get)
        #print(max_key)
        return max_key