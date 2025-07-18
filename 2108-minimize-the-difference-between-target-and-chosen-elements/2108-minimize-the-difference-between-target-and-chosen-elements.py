class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        n = len(mat)
        m = len(mat[0])
        dp = [set() for _ in range(n)]
        dp[0] = set(mat[0])

        for i in range(1,n):
            temp = set()
            for j in range(m):
                for item in dp[i-1]:
                    temp.add(item + mat[i][j])
            dp[i] = temp
        res = set(abs(val-target) for val in dp[n-1])
        return min(res)