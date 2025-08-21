class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        res = [0]*(n+1)
        carry = 1

        for i in range(n-1,-1,-1):
            res[i+1] = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10

        res[0] = carry
        #print(res)
        return res if res[0] else res[1:]