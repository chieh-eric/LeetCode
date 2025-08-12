class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        heights = [[0]*m for _ in range(n)]

        for j in range(m):
            cur = 0
            for i in range(n):
                if matrix[i][j] == "0":
                    cur = 0
                    continue
                cur += int(matrix[i][j])
                heights[i][j] = cur

        for i in range(n):
            heights[i].append(0)

        #print(heights)

        max_val = 0
        for height in heights:
            stack = []
            for i, hi in enumerate(height):

                while stack and height[stack[-1]] > hi:
                    idx = stack.pop()
                    width = i
                    if stack:
                        width = i - stack[-1] - 1
                    max_val = max(max_val, width*height[idx])
                stack.append(i)
        return max_val
        