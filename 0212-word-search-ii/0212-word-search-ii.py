class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        
        m = len(board)
        n = len(board[0])


        def dfs(i,j, index):
            if index == l-1:
                return True
            #print(i,j,word)
            found = False
            visited.add((i,j))
            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and board[nx][ny] == word[index+1]:
                        found = found or dfs(nx, ny, index+1)
            visited.remove((i,j))
            return found

        ans = []
        for word in words:
            l = len(word)
            visited = set()
            find = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if dfs(i,j,0):
                            ans.append(word)
                            find = True
                            break
                if find:
                    break
        return ans

        #["a","b","c"],
        #["a","e","d"],
        #["a","f","g"]]

        


        