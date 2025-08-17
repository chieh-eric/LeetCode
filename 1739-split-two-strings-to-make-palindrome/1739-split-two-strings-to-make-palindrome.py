class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        n = len(a)
            
        def check(x,y):
            left = 0
            right = n - 1
            while left < n and right < n and x[left] == y[right]:
                left += 1
                right -= 1
            
            remaina = a[left:right+1]
            remainb = b[left:right+1]
            return remaina == remaina[::-1] or remainb == remainb[::-1]


        return check(a,b) or check(b,a)