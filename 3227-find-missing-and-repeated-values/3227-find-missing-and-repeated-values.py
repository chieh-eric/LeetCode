class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        exist = Counter()
        n = len(grid)
        exist = [False]*((n**2) + 1)
        exist[0] = True

        a = b = -1
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if not exist[val]:
                    exist[val] = True
                else:
                    a = val
        
        for i in range(1,n**2+1):
            if not exist[i]:
                b = i
                break
        return [a,b]