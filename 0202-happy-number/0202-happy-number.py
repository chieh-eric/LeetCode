class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = {}
        def find(n):
          
            if n == 1:
                return True

            memo[n] = False
            count = 0
            s = str(n)
            for i in range(len(s)):
                count += (int(s[i]))**2
            
            if count in memo:
                return False
            
            return find(count)
        #find(n)
        return find(n)