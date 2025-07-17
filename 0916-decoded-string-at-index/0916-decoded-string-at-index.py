class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for i in range(len(s)):
            if s[i].isdigit():
                size *= int(s[i])
            else:
                size += 1
        #print(size)
        for i in range(len(s)-1,-1,-1):
            ch = s[i]
            k %= size
            
            if k == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1