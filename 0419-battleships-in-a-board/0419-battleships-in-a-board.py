class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = len(board)
        m = len(board[0])

        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def bfs(i,j):
            queue = deque([(i,j)])
            while queue:
                x, y = queue.popleft()
                board[x][y] = "."
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "X":
                        queue.append((nx,ny))


        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    count += 1
                    bfs(i,j)
        return count