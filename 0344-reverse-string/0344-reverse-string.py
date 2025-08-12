class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse(i,j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        reverse(0,len(s)-1)
        