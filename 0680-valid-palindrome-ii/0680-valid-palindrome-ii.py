class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        
        n = len(s)
        left = 0
        right = n - 1
        tolerance = 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        new_str_without_left = s[left+1:right+1]
        new_str_without_right = s[left:right]
        return new_str_without_left == new_str_without_left[::-1] or new_str_without_right == new_str_without_right[::-1]
        
        