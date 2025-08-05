class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1 110101
        # 3 000101
        # 6 000010
        # 8 000001
        # 9 000000
        total = 0
        n = len(s)
        prev = s[0]
        for i in range(1,n):
            if s[i] != prev:
                total += min(i,n-i)
            prev = s[i]
        return total