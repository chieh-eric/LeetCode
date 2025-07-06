import math
class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        common = a*b // gcd(a,b)
        #print(common)
        mod = 10**9 + 7


        numToCommon = common // a + common // b - 1
        #print(numToCommon)

        times = n // numToCommon
        #print(times)
        remain = n % numToCommon
        #print(remain)
        a_index = b_index = 1
        res = 0
        while remain > 0:
    
            if a_index*a < b_index*b:
                res = a_index*a
                a_index += 1
            else:
                res = b_index*b
                b_index += 1
            #print(res)
            remain -= 1

        return ((times*common) + res) % mod