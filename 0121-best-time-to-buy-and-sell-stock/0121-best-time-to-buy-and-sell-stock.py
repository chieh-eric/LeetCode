class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = float('inf')
        max_profix = 0

        for price in prices:
            if price < min_val:
                min_val = price
            else:
                max_profix = max(max_profix, price - min_val)
        return max_profix


        