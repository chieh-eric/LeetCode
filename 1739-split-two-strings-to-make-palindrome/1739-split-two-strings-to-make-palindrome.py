class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def isPalindrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def check(x,y):
            l = 0
            r = len(y) - 1
            while l < r and x[l] == y[r]:
                l += 1
                r -= 1
            return isPalindrome(x,l,r) or isPalindrome(y,l,r)

        return check(a,b) or check(b,a)