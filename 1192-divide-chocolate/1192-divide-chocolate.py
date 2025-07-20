class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        right = sum(sweetness) // (k+1)
        left = 0
        
        while left < right:
            mid = (left+right+1) // 2
            cur = 0
            cut = 0
            for swe in sweetness:
                cur += swe
                if cur >= mid:
                    cut += 1
                    cur = 0
            if cut < (k+1):
                right = mid - 1
            else:
                left = mid 
        return left       