import heapq
class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((0, start[0], start[1]))
        rank = []
        visited = set()
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        while queue:
      
            d, r, c = queue.popleft()
            if grid[r][c] > 1:
                if pricing[0] <= grid[r][c] <= pricing[1]:
                    heapq.heappush(rank,(d+1,grid[r][c],r,c))
            visited.add((r,c))
            for dx, dy in direction:
                nx = r + dx
                ny = c + dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] != 0:
                    visited.add((nx,ny))
                    queue.append((d+1, nx, ny))
            
            #print(temp)
        ans = []
        i = 0
        #print(rank)
        while i < k and rank:
            _, _, r, c = heapq.heappop(rank)
            ans.append((r,c))
            i += 1
        return ans

            