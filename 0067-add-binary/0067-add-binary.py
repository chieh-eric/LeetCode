class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        if n < m:
            a = "0"*(m-n) + a
        
        if n > m:
            b = "0"*(n-m) + b
        
        carry = 0
        r = ""
        #print(a)
        #print(b)
        for i in range(max(n,m)-1, -1, -1):
            #print(a[i])
            #print(b[i])
            res = (int(a[i]) + int(b[i]) + carry) % 2
            carry = (int(a[i]) + int(b[i]) + carry) // 2
            
            r = str(res) + r 
            #print(r)
        #print(r)
        
        if carry == 1:
            r = "1" + r
        return r