class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def build(length):
            res = []
            cur = 1
            while len(bin(cur)[2:]) <= length:
                res.append(str(bin(cur)[2:]))
                cur = cur*5
            return res
        n = len(s)
        if n == 1 and s[0] == "0":
            return -1
        elif n == 1 and s[0] == "1":
            return 1
        
        possible = build(n)
        #print(possible)
        dp = [float('inf')]*(n+1)
        # Initial Case:
        dp[0] = 0

        # Recursive form
        for i in range(1,n+1):
            for candidate in possible:
                l = len(candidate)
                #print(i)
                if  l > i:
                    break
                if s[i-l:i] == candidate:
                    #print("hi")
                    #print(candidate)
                    if i < n and s[i] == "0":
                        continue
                    dp[i] = min(dp[i], dp[i-l] + 1)
        
        #print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1