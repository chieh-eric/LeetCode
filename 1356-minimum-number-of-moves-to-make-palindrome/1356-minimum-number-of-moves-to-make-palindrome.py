from collections import defaultdict
class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
    
        def dfs(s):
            m = len(s)
            if  m <= 1:
                return 0
            
            i = m - 1
            while s[0] != s[i]:
                i -= 1
            
            if i == 0:
                return m // 2 + dfs(s[1:])

            return (m-1-i) + dfs(s[1:i]+s[i+1:])                

        
        return dfs(s)