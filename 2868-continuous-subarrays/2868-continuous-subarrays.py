class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        max_queue = deque()
        min_queue = deque()
        
        res = 0
        left = 0
        for right in range(n):

            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[right])

            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > 2:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
                
            
            res += (right - left + 1)
        return res