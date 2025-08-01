class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        queue = deque([(entrance[0],entrance[1],0)])

        shortest = float('inf')
        first = True
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(maze)
        m = len(maze[0])
        visited = set()
        while queue:
            #print(queue)
            i, j, step = queue.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and maze[nx][ny] != "+":
                    queue.append((nx,ny,step+1))
                
                if (nx == -1 or nx == n or ny == -1 or ny == m) and not first:
                    return step
            first = False
        return -1