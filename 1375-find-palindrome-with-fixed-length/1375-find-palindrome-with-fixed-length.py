class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        half = (intLength+1)/2
        total = (10**half) - (10**(half-1))
        ans = []

        def find(target):
            pos = str((10**(half-1)) + (target-1))
            if intLength % 2:
                temp = pos[::-1]
                ret = pos + temp[1:]
            else:
                ret = pos + pos[::-1]
                
            return int(ret)
        for q in queries:
            if q > total:
                ans.append(-1)
            else:
                ans.append(find(q))
        return ans
