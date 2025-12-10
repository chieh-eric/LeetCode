class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                popIndex = stack.pop()
                if stack:
                    res += ((min(height[stack[-1]], h) - height[popIndex])*(i-stack[-1]-1))
            stack.append(i)
        return res