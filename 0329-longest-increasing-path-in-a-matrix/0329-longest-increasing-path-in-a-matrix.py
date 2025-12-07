class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        memo = {}
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            max_val = 1
            logest_val = 0
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] > matrix[i][j]:
                    logest_val = max(logest_val, dfs(nx, ny))
            max_val += logest_val
            memo[(i,j)] = max_val
            return max_val

        path = 0
        for i in range(n):
            for j in range(m):
                path = max(path, dfs(i,j))
                #print(i, j, path)
        return path
        