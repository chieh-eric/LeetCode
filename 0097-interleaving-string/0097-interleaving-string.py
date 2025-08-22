class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        index1 = index2 = index3 = 0
        n = len(s1)
        m = len(s2)
        o = len(s3)
        if m + n != o:
            return False
        memo = {}
        def dp(i,j,k):
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            if i == n and j == m and k == o:
                return True

            res = False
            if i < n and s1[i] == s3[k]:
                res = res or dp(i+1, j, k+1)
            
            if j < m and s2[j] == s3[k]:
                res = res or dp(i, j+1, k+1)
            
            memo[(i,j,k)] = res
            return res
        return dp(0,0,0)
