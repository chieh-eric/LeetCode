class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cur = n
        while cur > 0:
            if cur == 1:
                return True
            if cur % 2:
                return False
            cur /= 2
        return cur > 0