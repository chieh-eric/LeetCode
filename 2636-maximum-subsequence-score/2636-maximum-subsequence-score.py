import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums1)
        pair = [(nums2[i],nums1[i]) for i in range(n)]

        pair.sort()
        cur_sum = 0
        heap = []
        max_val = 0
        for nums2_i, nums1_i in reversed(pair):
            cur_sum += nums1_i
            heapq.heappush(heap,nums1_i)

            if len(heap) > k:
                val = heapq.heappop(heap)
                cur_sum -= val
            if len(heap) == k:
                max_val = max(max_val, cur_sum*nums2_i)
        return max_val