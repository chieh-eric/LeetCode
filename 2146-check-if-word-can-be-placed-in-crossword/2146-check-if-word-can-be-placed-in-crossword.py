class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        l = len(word)
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def check(i,j,index,d):
            if index == l:
                if board[i][j] == "#":
                    return True
                else:
                    return False
            if board[i][j] == " " or board[i][j] == word[index]:
            
                nx = i + direction[d][0]
                ny = j + direction[d][1]
                # print("inside")
                # print(i,j)
                # print(d)
                # print(nx,ny)
                if 0 <= nx < m and 0 <= ny < n:
                    
                    return check(nx,ny,index+1,d)
                else:
                    # print("fucxk")
                    # print(direction[d])
                    # print(nx,ny)
                    if index == l - 1:
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == " " or board[i][j] == word[0]:
                    # Down
                    if i == 0 or (i > 0 and board[i-1][j] == "#"):
                        if check(i,j,0,0):
                            #print("hi")
                            return True
                    # Up
                    if i == m - 1 or (i < m - 1 and board[i+1][j] == "#"):
                        # print("start")
                        # print(i,j)
                        if check(i,j,0,1):
                            # print(i,j)
                            # print("h1i")
                            return True
                    # Right
                    if j == 0 or (j > 0 and board[i][j-1] == "#"):
                        if check(i,j,0,2):
                            #print("hi2")
                            return True
                    # Left
                    if j == n - 1 or (j < n - 1 and board[i][j+1] == "#"):
                        if check(i,j,0,3):
                            #print("h3")
                            return True
        return False