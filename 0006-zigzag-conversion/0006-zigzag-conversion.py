class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        rows = ['']*numRows

        cur = 0
        d = 1

        for ch in s:
            rows[cur] += ch

            if cur == 0:
                d = 1
            elif cur == numRows - 1:
                d = -1
            cur += d
        return ''.join(rows)