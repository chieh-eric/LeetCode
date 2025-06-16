class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        n = len(weights)
        def check(capacity):
            cur = 0
            day = 1
            for i in range(n):
                
                if cur + weights[i] > capacity:
                    cur = 0 
                    day += 1
                cur += weights[i]
            return day

        max_val = total = 0
        for i in range(n):
            total += weights[i]
            if weights[i] > max_val:
                max_val = weights[i]


        left = max_val
        right = total
        
        while left < right:
            mid = (left+right) // 2
            res = check(mid)

            if res > days:
                left = mid + 1
            else:
                right = mid

        return left