class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        n = len(heights)
   
        stack = [-1]
        max_val = 0
        #print(heights)
        for i in range(n):
            op = 0
            #print("start")
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                width = i - stack[-1] - 1
                
                max_val = max(max_val, width*heights[index])
                #print(max_val)
            #print(stack)
            stack.append(i)
            #print(stack)
            #print(max_val)
        return max_val