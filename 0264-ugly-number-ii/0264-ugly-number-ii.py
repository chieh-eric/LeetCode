import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = []
        heap = [1]
        count = 0
        cur = 0
        used = set()
        while count < n:
            count += 1
            #print(heap)
            cur = heapq.heappop(heap)
            #print(cur)
            if cur*2 not in used:
                heapq.heappush(heap, cur*2)
                used.add(cur*2)
            if cur*3 not in used:
                used.add(cur*3)
                heapq.heappush(heap, cur*3)
            if cur*5 not in used:
                used.add(cur*5)
                heapq.heappush(heap, cur*5)
        return cur

        

        