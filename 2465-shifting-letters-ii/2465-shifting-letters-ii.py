class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        change = [0]*(n+1)
        res = []
        for start, end, d in shifts:
            if d == 1:
                change[start] +=1
                change[end+1] -= 1
            else:
                change[start] -=1
                change[end+1] += 1
        final = []
        cum = 0
        for i in range(n):
            cum += change[i]
            final.append(cum)

        for i in range(n):
            shift = (ord(s[i])-ord('a')+final[i])%26
            new_char = chr(ord('a')+shift)
            res.append(new_char)
        return ''.join(res)
