class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        def calculate(val):
            count = 0
            for p in piles:
                count += (p+val-1) // val
            return count

        while left < right:
            mid = (left+right) // 2
            res = calculate(mid)

            if res > h:
                left = mid + 1
            else:
                right = mid
        return left