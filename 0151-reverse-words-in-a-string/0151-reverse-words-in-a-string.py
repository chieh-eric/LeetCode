class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = " "+ s[::-1]
        i = 0
        n = len(s)
        
        res = ""
        while i < n:

            while i < n and s[i] == " ":
                i += 1
            
            start = i
            while i < n and s[i] != " ":
                i += 1

            if s[i-1 : start-1 : -1]:
                res += s[i-1 : start-1 : -1] +" "
        #print(res)
        return res[:-1]