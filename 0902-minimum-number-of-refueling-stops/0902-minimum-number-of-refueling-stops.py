import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.sort()
        heap = []
        i = 0
        n = len(stations)
        current = startFuel
        if startFuel >= target:
            return 0

        step = 0
        while i < n or heap:
            
            while i < n and current >= stations[i][0]:
                heapq.heappush(heap,-stations[i][1])
                i += 1
            step += 1
            if heap:
                val = -heapq.heappop(heap)
                current += val
            else:
                return -1
        
            if current >= target:
                return step
        return -1
                