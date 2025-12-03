import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        queue = []
        n = len(heightMap)
        m = len(heightMap[0])
        for i in range(n):
            heapq.heappush(queue,(heightMap[i][0], i, 0))
            heightMap[i][0] = -1
        
        for i in range(n):
            heapq.heappush(queue,(heightMap[i][m-1], i, m-1))
            heightMap[i][m-1] = -1
        
        for i in range(m):
            heapq.heappush(queue,(heightMap[0][i], 0, i))
            heightMap[0][i] = -1
        
        for i in range(m):
            heapq.heappush(queue,(heightMap[n-1][i], n-1, i))
            heightMap[n-1][i] = -1
        
        trap = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            lowest, x, y = heapq.heappop(queue)
            
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < n and 0 <= ny < m and heightMap[nx][ny] != -1:
                    if heightMap[nx][ny] < lowest:
        
                        trap += (lowest - heightMap[nx][ny])
                    heapq.heappush(queue, (max(lowest,heightMap[nx][ny]), nx,ny))
                  
                    heightMap[nx][ny] = -1
        return trap


        
        