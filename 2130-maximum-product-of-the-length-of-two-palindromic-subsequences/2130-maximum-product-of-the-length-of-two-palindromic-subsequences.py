class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.max_product = 0

        def isPalindrome(t):
            l = 0
            r = len(t) - 1
            while l < r:
                if t[l] != t[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        self.s1 = []
        self.s2 = []
        n = len(s)

        def backtrack(i):
           
            if i == n:
                if isPalindrome("".join(self.s1)) and isPalindrome("".join(self.s2)):
                    self.max_product = max(self.max_product, len(self.s1)*len(self.s2))
                return
            
            for j in range(3):
                if j == 1:
                    self.s1.append(s[i])
                    backtrack(i+1)
                    self.s1.pop()
                    if not self.s1:
                        break
                    
                elif j == 2:
                    self.s2.append(s[i])
                    backtrack(i+1)
                    self.s2.pop()
                    if not self.s2:
                        break
                else:
                    backtrack(i+1)

                
        backtrack(0)
        return self.max_product
                