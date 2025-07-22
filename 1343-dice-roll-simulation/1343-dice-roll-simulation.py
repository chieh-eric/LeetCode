class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # dp(index,state) means under this situation, the maximum distinct sequence
        mod = 10**9 + 7
        memo = {}
        def dp(index, prev, count):
            if index == n:
                return 1
            if (index, prev, count) in memo:
                return memo[(index, prev, count)]
                
            cur = 0
            for i in range(6):
                if i == prev:
                    if count < rollMax[i]:
                        cur += dp(index+1,i,count+1)
                else:
                    cur += dp(index+1,i,1) % mod
            memo[(index, prev, count)] = cur
            return cur % mod
        return dp(0,-1,0) % mod