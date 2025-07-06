class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        n = len(nums)
        op = 0
        for i in range(n):
            
            while stack and stack[-1] > nums[i]:
                    stack.pop()
            if not stack or stack[-1] < nums[i]:
                if nums[i] > 0:
                    op += 1
                stack.append(nums[i])
                
                
        return op
            