class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        queue.append((0,(0,0),(0,1),0)) # step, tail, head, state (0 represent horizon, 1 represent vertical)
        visited = set()
        n = len(grid)
        direction = [(0,1),(1,0)]
        clockwise = [1,-1]
        while queue:
            step, (tail_x,tail_y), (head_x,head_y), state = queue.popleft()

            if ((tail_x,tail_y),(head_x,head_y)) in visited:
                continue
            
            visited.add(((tail_x,tail_y),(head_x,head_y)))
            for dx, dy in direction:
                tail_nx = tail_x + dx
                tail_ny = tail_y + dy

                head_nx = head_x + dx
                head_ny = head_y + dy

                if 0 <= tail_nx < n and 0 <= tail_ny < n and 0 <= head_nx < n and 0 <= head_ny < n:
                    if (tail_nx,tail_ny) == (n-1,n-2) and (head_nx,head_ny) == (n-1,n-1) or (tail_nx,tail_ny) == (n-1,n-1) and (head_nx,head_ny) == (n-1,n-2):
                        return step + 1
                    if grid[tail_nx][tail_ny] == 0 and grid[head_nx][head_ny] == 0:
                        queue.append((step+1,(tail_nx,tail_ny),(head_nx,head_ny),state))

            if state:
                head_nx = tail_x
                head_ny = tail_y + 1
            else:
                head_nx = tail_x + 1
                head_ny = tail_y
            if 0 <= head_nx < n and 0 <= head_ny < n:
                if grid[tail_x+1][tail_y+1] != 1 and grid[head_nx][head_ny] != 1:
                    queue.append((step+1,(tail_x,tail_y),(head_nx,head_ny),state^1))
        return -1
