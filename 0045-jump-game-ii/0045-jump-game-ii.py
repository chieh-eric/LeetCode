class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        farthest = currentEnd = 0
        step = 0
        for i in range(n-1):
            
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                currentEnd = farthest
                step += 1
        return step