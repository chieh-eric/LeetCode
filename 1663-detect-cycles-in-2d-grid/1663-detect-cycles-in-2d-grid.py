class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[0]*n for _ in range(m)]
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j,parent,letter):
            if visited[i][j] == 2:
                return False
            
            if visited[i][j] == 1:
                return True

            visited[i][j] = 1

            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if parent and nx == parent[0] and ny == parent[1]:
                        continue
                    
                    if visited[nx][ny] != 2 and grid[nx][ny] == letter:
                        #print(grid[i][j])
                        #print(letter)
                        if dfs(nx,ny,(i,j),letter):
                            return True
            visited[i][j] = 2
            return False
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    #print(i,j)
                    #print(visited)
                    
                    if dfs(i,j,None,grid[i][j]):
                        return True
        return False

        # ["f","a","a","c","b"],
        # ["e","a","a","e","c"],
        # ["c","f","b","b","b"],
        # ["c","e","a","b","e"],
        # ["f","e","f","b","f"]]
