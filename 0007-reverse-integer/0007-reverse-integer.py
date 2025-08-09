class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x >= 0:
            val = int(s[::-1])
            if val > 2**31 -1:
                return 0
            return val
        else:
            val = -int(s[:0:-1])
            if val < -2**31:
                return 0
            return val