class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """
        # Two Way
        # 1. Use Root to catch queen, another one is wall
        # 2. Use Bishop to catch queen, another one is wall
        
        if a == e:
            if c != e:
                return 1
            if not (min(b,f) < d < max(b,f)):
                return 1
        
        if b == f:
            if d != f:
                return 1
            if not (min(a,e) < c < max(a,e)):
                return 1
        
        if abs(c-e) == abs(d-f):
            if not (abs(a-e) == abs(b-f) and min(c,e) < a < max(c,e) and min(d,f) < b < max(d,f)):
                return 1
        return 2
        
        # (1,6)
        # (3,3)
        # (5,6)
