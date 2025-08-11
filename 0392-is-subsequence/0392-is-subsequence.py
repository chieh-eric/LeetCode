class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        n = len(s)
        t_index = 0
        m = len(t)

        while s_index < n and t_index < m:
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1
        return s_index == n