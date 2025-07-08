class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(d):
            if d < 2:
                return False
            if d == 2:
                return True
            if not d % 2:
                return False

            for i in range(3,int(d**0.5)+1,2):
                if not d % i:
                    return False
            return True
        
        if 7 < n < 12:
            return 11
        else:
            val = n
            l = len(str(n))
            if l % 2 == 0:
                half = (l+1) // 2 + 1
                for start in range(10**(half-1),10**half):
                    s = str(start)
                    pal = int(s+s[-2::-1])
                    if isPrime(pal):
                        return pal

            else:
                half = (l+1) // 2
                init = int(str(n)[:half])
               
                for start in range(init,10**half):
                    s = str(start)
                    pal = int(s+s[-2::-1])
                    if pal >= n and isPrime(pal):
                        return pal

                for start in range(10**(half),10**(half+1)):
                    s = str(start)
                    pal = int(s+s[-2::-1])
                    if pal >= n and isPrime(pal):
                        return pal
                