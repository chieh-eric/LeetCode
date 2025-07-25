import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """

        pair = [(efficiency[i],speed[i]) for i in range(n)]
        pair.sort()
        mod = 10**9 + 7
        res = []
        max_sum = cur_sum = 0
        for eff_i, speed_i in reversed(pair):
            cur_sum += speed_i
            heapq.heappush(res,speed_i)

            if len(res) > k:
                p = heapq.heappop(res)
                cur_sum -= p

            max_sum = max(max_sum,cur_sum*eff_i)
        return max_sum % mod