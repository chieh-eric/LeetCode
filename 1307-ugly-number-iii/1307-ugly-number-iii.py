class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(x,y):
            while y:
                x, y = y, x % y
            return x
        
        def f(x):
            a_b = a*b/gcd(a,b)
            a_c = a*c/gcd(a,c)
            b_c = b*c/gcd(b,c)
            all_common = a*(b_c)/gcd(a,b_c)

            count_a = x // a
            count_b = x // b
            count_c = x // c

            minus_ab = x // a_b
            minus_ac = x // a_c
            minus_bc = x // b_c
            add_all_common = x // all_common

            return count_a + count_b + count_c - minus_ab - minus_ac - minus_bc + add_all_common

        b_c = b*c/gcd(b,c)
        base = a*(b_c)/gcd(a,b_c)
        count = f(base)
        multiply = n // count
        remain = n % count

        left = 0
        right = base
        
        while left < right:
            mid = (left+right) // 2
            target = f(mid)
            if target < remain:
                left = mid + 1
            else:
                right = mid

        #print(left)
        #print(f(6))
        return base*multiply + left
        

