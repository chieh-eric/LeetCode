class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = set(mat[0])
        n = len(mat)
        for i in range(1,n):
            res &= set(mat[i])
        return min(list(res)) if res else -1
            