class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        count = 0
        for num in nums:

            while stack and stack[-1] > num:
                stack.pop()
                count += 1
            
            if (not stack or stack[-1] < num) and num != 0:
                stack.append(num)
        return count + len(stack)