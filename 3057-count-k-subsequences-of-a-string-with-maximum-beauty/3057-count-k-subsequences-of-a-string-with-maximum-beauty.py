import math
class Solution(object):
    def countKSubsequencesWithMaxBeauty(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        count = Counter(s)
        if len(count) < k:
            return 0
        
        bar = sorted(count.values())[-k]
        res = 1
        m = 0

        def comb(n, k):
            
            return math.factorial(n) // (math.factorial(n-k)*math.factorial(k))

        for v in count.values():
            if v > bar:
                k -= 1
                res = res*v % mod
            
            if v == bar:
                m += 1

        return res*comb(m,k)*pow(bar,k,mod) % mod