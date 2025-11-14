class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        # Approach
        # 1. numVistedRow = matrix row
        # 2. numVisitedCol = matrix col
        # 3. Finished all queries

        # Worst TC -> O(len(queries)*n)
        ans = 0
        visited_row = {}
        visited_col = {}
        numVistedRow = 0
        numVisitedCol = 0

        for t, idx, val in reversed(queries):
            if numVistedRow == n or numVisitedCol == n:
                break
            # Row
            if t == 0:
                if idx in visited_row:
                    continue
                visited_row[idx] = True
                numVistedRow += 1
                ans += (val) * (n-len(visited_col))
            # Col
            else:
                if idx in visited_col:
                    continue
                visited_col[idx] = True
                numVisitedCol += 1
                ans += val * (n-len(visited_row))
            #print(ans)
        return ans
