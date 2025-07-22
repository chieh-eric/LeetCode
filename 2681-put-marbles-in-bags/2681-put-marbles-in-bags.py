import heapq
class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        small = []
        large = []
        for i in range(n-1):
            heapq.heappush(small,weights[i]+weights[i+1])
            heapq.heappush(large,-weights[i]-weights[i+1])
        
        larger = 0
        smaller = 0
        for i in range(k-1):
            lar = -heapq.heappop(large)
            larger += lar

            sma = heapq.heappop(small)
            smaller += sma
        return larger - smaller