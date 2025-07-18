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
        for cur_day in range(1,10**5+1):
            while  index < n and cur_day >= events[index][0]:
                heapq.heappush(heap,events[index][1])
                index += 1

            while heap and cur_day > heap[0]:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                attend += 1
            elif not heap and index == n:
                break
        return attend
                