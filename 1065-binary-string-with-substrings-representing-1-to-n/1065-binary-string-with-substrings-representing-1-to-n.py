class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        max_len = len(bin(n)) - 2
        seen = set()
        for l in range(1,max_len+1):
            for i in range(len(s)-l+1):
                num = int(s[i:i+l],2)
                if num <= n and num != 0:
                    seen.add(num)
        return len(seen) == n