class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(heights)
        res = [0]*n
        for i in range(n-1,-1,-1):
            
            op = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                op += 1
            if stack:
                op += 1
            stack.append(heights[i])
            res[i] = op
        return res