class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        n = len(s)
        if n < minSize:
            return 0
        left = 0
        cur = {}
        substr = {}

        # Expand: size smaller than minSize, check limitation
        for i in range(n):
            cur[s[i]] = cur.get(s[i],0) + 1

            while len(cur) > maxLetters or i - left >= minSize:
                cur[s[left]] -= 1
                if cur[s[left]] == 0:
                    del cur[s[left]]
                left += 1
            
            if i - left + 1 == minSize:
                substr[s[left:i+1]] = substr.get(s[left:i+1],0) + 1
            
           
        return max(substr.values()) if substr else 0