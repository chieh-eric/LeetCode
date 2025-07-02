from itertools import permutations
class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        min_s = None
        
        def merge(s1,s2):
            if s1 in s2:
                return s2
            if s2 in s1:
                return s1

            overlap = 0
            for i in range(1,min(len(s1),len(s2))+1):
                if s1[-i:] == s2[:i]:
                    overlap = i
            return s1 + s2[overlap:]
       
        for perm in permutations([a,b,c]):
            m = merge(merge(perm[0],perm[1]),perm[2])
            if min_s is None or len(m) < len(min_s) or (len(m) == len(min_s) and m < min_s):
                min_s = m

        return min_s