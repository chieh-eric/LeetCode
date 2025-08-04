import heapq
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        free_server = SortedList()
        for i in range(k):
            free_server.add(i)
        occupy = []
        count_usage = Counter()
        n = len(arrival)
        combine = [(arrival[i],load[i], i) for i in range(n)]
        combine.sort()
        for time, duration, i in combine:
            while occupy and occupy[0][0] <= time:
                _, server = heapq.heappop(occupy)
                free_server.add(server)
            if not free_server:
                continue
           
            idx = free_server.bisect_left(i%k)
           
            idx = 0 if idx == len(free_server) else idx
            
            count_usage[free_server[idx]] += 1
            heapq.heappush(occupy, (time+duration,free_server[idx]))
            free_server.pop(idx)
          
        max_val = max(count_usage.values())
        res = []
        #print(count_usage)
        for key in count_usage:
            if count_usage[key] == max_val:
                res.append(key)
        return res
        # 2, 3, 1

        # 11
        # 9
        # 13

        # SortedList:
        # 0 1 2
        # 