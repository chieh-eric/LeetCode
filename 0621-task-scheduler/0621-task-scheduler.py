import heapq
from collections import defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        # heap -> (-remain, task)
        pq = []
        for task, num in count.items():
            heapq.heappush(pq, (-num, task))
        
        time = 0
        while pq:
            interval = n + 1
            tmp = []

            while interval > 0 and pq:
                neg_remain, task = heapq.heappop(pq)
                time += 1
                if neg_remain + 1 < 0:
                    tmp.append((neg_remain + 1, task))
                interval -= 1

            for remain, task in tmp:
                heapq.heappush(pq,(remain, task))
            
            if pq:
                time += interval
        return time