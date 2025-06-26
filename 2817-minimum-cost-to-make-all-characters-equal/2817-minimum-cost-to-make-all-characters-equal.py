class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Prefix -> Means in index i, the total cost of slipping(not include flip current index)
        n = len(s)
        prefix = [0]*n
        suffix = [0]*n

        prev = s[0]
        cost = 0
        for i in range(1,n):
            if prev != s[i]:
                cost += i
            prefix[i] = cost
            prev = s[i]

        nxt = s[-1]
        cost = 0
        for i in range(n-2,-1,-1):
            if nxt != s[i]:
                cost += (n-i-1)
            suffix[i] = cost
            nxt = s[i]

        return min(x+y for x, y in zip(prefix,suffix))