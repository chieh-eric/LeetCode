class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Stack -> (height, index)
        # Stack = [(2,3), (1,4), (0,5)]
        # water -> (height - stack[-1][0])*(index-stack[-1][1]) (if stack exist)
        stack = []
        trap = 0
        for i, h in enumerate(height):
            while stack and stack[-1][0] < h:
                pop_hight = stack[-1][0]
                stack.pop()
                if stack:
                    trap += (min(h,stack[-1][0]) - pop_hight)*(i-stack[-1][1]-1)
                #print(trap)
            stack.append((h, i))
        return trap