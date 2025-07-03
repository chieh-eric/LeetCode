class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        n = len(a)
        mid = (n+1) // 2
        if a == a[::-1] or b == b[::-1]:
            return True

        def isPalindrome(s):
            return s == s[::-1]
        pivot = 0
        for i in range(n):
            if a[:i] == b[n-1:-i-1:-1]:
                pivot = i
            else:
                break
        
        if pivot != 0 and isPalindrome(a[:pivot]+b[pivot:]):
            return True
        if pivot != 0 and isPalindrome(a[:-pivot]+b[-pivot:]):
            return True

        pivot = 0
        for i in range(n):
            if b[:i] == a[n-1:-i-1:-1]:
                pivot = i
            else:
                break
        
        if pivot != 0 and isPalindrome(b[:pivot]+a[pivot:]):
            return True
        if pivot != 0 and isPalindrome(b[:-pivot]+a[-pivot:]):
            return True

        return False