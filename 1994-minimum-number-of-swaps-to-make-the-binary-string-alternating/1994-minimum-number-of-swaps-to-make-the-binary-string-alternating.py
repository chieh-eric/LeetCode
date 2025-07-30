class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count_0 = s.count("0")
        count_1 = s.count("1")
        if abs(count_0-count_1) > 1:
            return -1
        
        op = 0
        odd = even = 0
        if count_0 == count_1:
            for i in range(n):
                if s[i] == "0" and i % 2:
                    odd += 1
                elif s[i] == "0" and i % 2 == 0:
                    even += 1
            op = min(odd,even)
        elif count_0 > count_1:
            for i in range(0,n,2):
                if s[i] != "0":
                    odd += 1
            op = odd
        else:
            for i in range(0,n,2):
                if s[i] != "1":
                    odd += 1
            op = odd
        return op
