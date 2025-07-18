class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        visited = [False]*((n**2)+1)
        mapping = {}

        val = 1
        if n % 2:
            for i in range(n-1,-1,-1):
                if i % 2 == 0:
                    for j in range(n):
                        mapping[val] = (i,j)
                        val += 1
                else:
                    for j in range(n-1,-1,-1):
                        mapping[val] = (i,j)
                        val += 1
        else:
            for i in range(n-1,-1,-1):
                if i % 2:
                    for j in range(n):
                        mapping[val] = (i,j)
                        val += 1
                else:
                    for j in range(n-1,-1,-1):
                        mapping[val] = (i,j)
                        val += 1


        queue = deque()
        queue.append((0,1))
        target = n**2
        #print(mapping)
        while queue:
            #print(queue)
            step, value = queue.popleft()
            if value == target:
                return step
            if visited[value]:
                continue

            visited[value] = True
            for k in range(value+1, min(value+6,n**2)+1):                  
                if k > n**2:
                    continue
                i, j = mapping[k]
                dest = board[i][j] if board[i][j] != -1 else k
                if not visited[dest]:
                    queue.append((step+1,dest))
        return -1