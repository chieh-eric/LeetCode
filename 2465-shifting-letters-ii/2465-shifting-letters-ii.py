class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        start = []
        for ch in s:
            start.append(ord(ch)-ord('a'))
     
            
        n = len(s)
        variable = [0]*(len(s)+1)
        for s, e, d in shifts:
            var = 1
            if d == 0:
                var = -1
            variable[s] += var
            variable[e+1] -= var
        
        cur = 0
        res = ""
        for i in range(n):
            cur += variable[i]
            start[i] = (start[i]+cur) % 26
            res += chr(ord('a')+start[i])
        return res