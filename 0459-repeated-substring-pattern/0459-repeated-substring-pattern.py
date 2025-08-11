class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        sub = ""
        for ch in s:
            sub += ch
            if n % len(sub) == 0 and n != len(sub):
                if sub*(n//len(sub)) == s:
                    return True
        return False