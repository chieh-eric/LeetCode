import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Largest freq first
        time = 0
        count = Counter(tasks)
        task_list = []
        for key, value in count.items():
            heapq.heappush(task_list, (-value, key))
        
        while task_list:
            neg_freq, ty = heapq.heappop(task_list)

            more = 0
            temp = []
            if neg_freq + 1 < 0:
                temp.append((neg_freq + 1, ty))
            while task_list and more < n:
                nxt_freq, ty = heapq.heappop(task_list)
                if nxt_freq + 1 < 0:
                    temp.append((nxt_freq+1, ty))
                more += 1
            if temp:
                time += (1+n)
            else:
                time += (more+1)

            for freq, ty in temp:
                heapq.heappush(task_list, (freq, ty))
        return time