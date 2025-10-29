class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n //= 2
            count += 1
        return 2**count - 1