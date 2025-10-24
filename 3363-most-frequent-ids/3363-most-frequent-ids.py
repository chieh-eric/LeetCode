import heapq
from collections import defaultdict
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        # Approach
        # Dictionaty (Hashmap), key -> value for element; value -> freq
        # For each iteration, -> find key with the maximum value
        # O(N^2) -> directly loop over the dictionary
        # O(N log N) -> dictionary and heap
        # dictionary -> store the latest freq(value) for that key
        # heap -> (max heap of freq)

        n = len(nums)
        heap = []
        latest = defaultdict(int)

        ans = []
        for i in range(n):
            latest[nums[i]] += freq[i]
            heapq.heappush(heap, (-latest[nums[i]], nums[i]))

            while heap and latest[heap[0][1]] != -heap[0][0]:
                heapq.heappop(heap)
            
            if heap:
                ans.append(-heap[0][0])
            else:
                ans.append(0)

        return ans
