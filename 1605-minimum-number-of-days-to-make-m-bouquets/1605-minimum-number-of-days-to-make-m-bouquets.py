class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if n/k < m:
            return -1
        l = 1
        r = max(bloomDay)

        def check(day,m,k):
            cont = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    cont += 1
                else:
                    cont = 0
                
                if cont == k:
                    m -= 1
                    cont = 0
            return m <= 0
        
        while l < r:
            mid = (l+r) // 2
            if not check(mid,m,k):
                l = mid + 1
            else:
                r = mid
        return l

