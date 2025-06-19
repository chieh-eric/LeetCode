class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque()
        m = len(isWater)
        n = len(isWater[0])
        ans = [[-1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i,j,0))
                    ans[i][j] = 0
        
        while queue:
            i, j, depth = queue.popleft()
            direction = [(0,1),(1,0),(0,-1),(-1,0)]
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = depth + 1
                    queue.append((nx,ny,depth+1))
        return ans
        