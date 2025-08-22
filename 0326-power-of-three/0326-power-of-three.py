class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cur = n
        if n < 0:
            return False
        
        remain = 0
        while cur:
            if cur == 1:
                return True
            remain = cur % 3
            cur = cur // 3
            if remain and cur:
                return False

        return n != 0 and remain == 0
