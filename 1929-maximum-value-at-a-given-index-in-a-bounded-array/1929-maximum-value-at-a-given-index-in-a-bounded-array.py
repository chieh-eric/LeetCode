class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """

        def calculate(val):
            min_left = min(index, val -1)
            min_left_val = (val+val-min_left)*(min_left+1)//2 - val

            min_right = min(n-index-1, val-1)
            min_right_val = (val+val-min_right)*(min_right+1)//2 - val

            return min_left_val+min_right_val+val + 1*(index-min_left) + 1*(n-index-1-min_right)
        l = maxSum // n
        r = maxSum - l
        
        while l < r:
            mid = (l+r+1) // 2
            res = calculate(mid)
            if res > maxSum:
                r = mid - 1
            else:
                l = mid
        return l
        
