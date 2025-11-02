class Solution(object):
    def countUnguarded(self, n, m, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        unavailabe = set()
        wall = set()
        guard_and_wall = set()

        for i, j in walls:
            unavailabe.add((i,j))
            guard_and_wall.add((i,j))
        
        for i, j in guards:
            guard_and_wall.add((i,j))
        

        def dfs(i, j, d):
            unavailabe.add((i,j))
            
            if d == 0:
                if i + 1 < n and (i+1,j) not in guard_and_wall:
                    dfs(i+1, j, 1)
                if j + 1 < m and (i, j+1) not in guard_and_wall:
                    dfs(i, j+1, 2)
                if i - 1 >= 0 and (i-1, j) not in guard_and_wall:
                    dfs(i-1, j, 3)
                if j - 1 >= 0 and (i, j-1) not in guard_and_wall:
                    dfs(i, j-1, 4)

            elif d == 1:
                if i + 1 < n and (i+1,j) not in guard_and_wall:
                    dfs(i+1, j, 1)
            
            elif d == 2:
                if j + 1 < m and (i, j+1) not in guard_and_wall:
                    dfs(i, j+1, 2)
            
            elif d == 3:
                if i - 1 >= 0 and (i-1, j) not in guard_and_wall:
                    dfs(i-1, j, 3)

            elif d == 4:
                if j - 1 >= 0 and (i, j-1) not in guard_and_wall:
                    dfs(i, j-1, 4)

        for i, j in guards:
            dfs(i,j,0)
        # print(unavailabe)
        # print(len(unavailabe))
        # print(sorted(list(unavailabe)))
        return (m*n) - len(unavailabe)

        