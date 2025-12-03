class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        # [(1,0),(0,1),]
        # trap = (prevHeight - popOutHeight)*(index - prevIndex - 1)
        trap = 0
        for i, val in enumerate(height):
            while stack and stack[-1][0] < val:
                popOutHeight = stack[-1][0]
                stack.pop()
                if stack:
                    trap += (min(stack[-1][0],val) - popOutHeight)*(i - stack[-1][1] - 1)
                #print(trap)
            #print(trap)
            stack.append((val, i))
        return trap