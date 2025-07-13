import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        n = len(tasks)
        res = []
        busy = []        
        free = []

        for i, weight in enumerate(servers):
            heapq.heappush(free,(weight,i))
        
        time = 0
        for i, task in enumerate(tasks):
            time = max(time,i)
            
            while busy and time >= busy[0][0]:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(free,(weight,idx))
            
            if free:
                weight, idx = heapq.heappop(free)
                heapq.heappush(busy,(time+task, weight, idx))
                res.append(idx)
            else:
                t, weight, idx = heapq.heappop(busy)
                time = t
                heapq.heappush(busy,(time+task, weight, idx))
                res.append(idx)
            
        return res