import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        max_val = -float('inf')
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            max_val = max(max_val, lst[0])
        
        best_l = -float('inf')
        best_r = float('inf')

        while True:
            min_val, lid, idx = heapq.heappop(heap)
            if max_val - min_val < best_r - best_l:
                best_r = max_val
                best_l = min_val
            
            if idx + 1 == len(nums[lid]):
                break
            
            nxt_val = nums[lid][idx+1]
            heapq.heappush(heap, (nxt_val, lid, idx+1))

            max_val = max(max_val, nxt_val)
        return [best_l, best_r]

