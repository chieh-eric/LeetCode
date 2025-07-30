class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k > 1:
            return "".join(sorted(s))
        
        n = len(s)
        cur = s
        for i in range(1,n):
            new_str =  s[-i:] + s[:-i]
          
            if cur > new_str:
                cur = new_str
        return cur