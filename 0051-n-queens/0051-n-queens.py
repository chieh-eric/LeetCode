class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        col = set()
        dia1 = set()
        dia2 = set()
        placement = []

        def backtrack(row):
            if row == n:
                board = []
                for c in placement:
                    r = ["."]*n
                    r[c] = "Q"
                    board.append("".join(r))
                res.append(board)
                return
            
            for i in range(n):
                if i not in col and row+i not in dia1 and row-i not in dia2:
                    col.add(i)
                    dia1.add(row+i)
                    dia2.add(row-i)
                    placement.append(i)

                    backtrack(row+1)

                    placement.pop()
                    col.remove(i)
                    dia1.remove(row+i)
                    dia2.remove(row-i)
        backtrack(0)
        #print(res)
        return res
            