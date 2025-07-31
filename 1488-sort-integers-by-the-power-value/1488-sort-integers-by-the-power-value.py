class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        memo = {}
        def transform(val):
            if val in memo:
                return memo[val]
            if val == 1:
                return 1
            
            step = 0
            if val % 2 == 0:
                step = transform(val//2) + 1
            else:
                step = transform(3*val+1) + 1
            
            memo[val] = step
            return step
        
        arr = []
        l = hi - lo + 1
        index = 0
        for i in range(lo,lo+l):
            arr.append((transform(i),i))
        arr.sort(key=lambda x:(x[0],x[1]))
        return arr[k-1][1]
        