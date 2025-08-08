class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = [0]*n
        right = [0]*n

        max_left = max_right = 0
        for i in range(n):
            max_left = max(max_left,height[i])
            left[i] = max_left
        
        for i in range(n-1,-1,-1):
            max_right = max(max_right,height[i])
            right[i] = max_right
        #print(left)
        #print(right)
        total = 0
        for i in range(n):
            total += min(left[i],right[i]) - height[i]
        return total
