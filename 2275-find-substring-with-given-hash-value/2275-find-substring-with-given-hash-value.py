class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        def val(s):
            return ord(s) - ord('a') + 1
        
        n = len(s)
        res_index = 0
        curr_hash = 0
        power_k = pow(power,k,modulo)

        for i in range(n-1,-1,-1):
            curr_hash = (curr_hash*power+val(s[i])) % modulo

            if i + k < n:
                curr_hash = (curr_hash - (val(s[i+k]))*power_k) % modulo
            
            if i + k <= n and curr_hash == hashValue:
                res_index = i
        
        return s[res_index:res_index+k]