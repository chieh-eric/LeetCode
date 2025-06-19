class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        res = []
        def gray(n):
            return n^(n>>1)
        for i in range(2**n):
            res.append(gray(i))
        start_index = res.index(start)
        n = len(res)
        return res[start_index:n+1] + res[:start_index]