from collections import defaultdict
class Solution(object):
    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        letter = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != "." and matrix[i][j] != "#":
                    letter[matrix[i][j]].append((i,j))
        visited = [[False]*m for _ in range(n)]
        queue = deque()
        if matrix[0][0] == ".":
            queue.append((0,0,0,set()))
        else:
            for i, j in letter[matrix[0][0]]:
                if i != 0 or j != 0:
                    queue.append((0,i,j,set(matrix[i][j])))
            queue.append((0,0,0,set()))

        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        #print(letter)
        while queue:
            step, i, j, used = queue.popleft()

            if i == n - 1 and j == m - 1:
                return step
            
            if visited[i][j]:
                continue

            visited[i][j] = True

            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] != "#":
                    if matrix[nx][ny] != ".":
                        if matrix[nx][ny] not in used:
                            queue.append((step+1,nx,ny,used))
                            used.add(matrix[nx][ny])
                            for qi, qj in letter[matrix[nx][ny]]:
                                if qi != nx or qj != ny:
                                    queue.append((step+1,qi,qj,used))
                        else:
                            queue.append((step+1,nx,ny,used))
                    else:
                        queue.append((step+1,nx,ny,used))
        return -1

