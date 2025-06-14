class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = abs(x)
        y = abs(y)
        direction = [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]
        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        count = 0
        while queue:
            n = len(queue)
            count += 1
            for i in range(n):
                i, j = queue.popleft()
                if i == x and j == y:
                    return count - 1
                
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    
                    if (nx,ny) not in visited and  -2 <= nx <= x + 2 and -2 <= ny <= y+2:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
