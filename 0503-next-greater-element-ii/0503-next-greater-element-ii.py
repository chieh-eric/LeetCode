class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        nums += nums
        stack = []
        ans = [-1]*m

        for i, val in enumerate(nums):
            while stack and stack[-1][0] < val:
                _, idx = stack.pop()
                if idx < m:
                    ans[idx] = val
            stack.append((val, i))
        return ans

        