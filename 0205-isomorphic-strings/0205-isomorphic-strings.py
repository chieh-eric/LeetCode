from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper1 = {}
        mapper2 = {}
        n = len(s)
        for i in range(n):
            if s[i] not in mapper1:
                mapper1[s[i]] = t[i]

            if t[i] not in  mapper2:
                mapper2[t[i]] = s[i]

            if mapper1[s[i]] != t[i]:
                return False
            
            if mapper2[t[i]] != s[i]:
                return False
                
        return True