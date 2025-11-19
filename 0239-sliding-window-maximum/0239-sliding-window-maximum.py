class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # [7]
        n = len(nums)
        max_queue = deque()
        for i in range(k):
            if not max_queue:
                max_queue.append(nums[i])
            else:
                while max_queue and max_queue[-1] < nums[i]:
                    max_queue.pop()
                max_queue.append(nums[i])

        res = [max_queue[0]]
        left = 0
        for i in range(k, n):
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            left += 1
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])
            res.append(max_queue[0])
        return res
            

                
