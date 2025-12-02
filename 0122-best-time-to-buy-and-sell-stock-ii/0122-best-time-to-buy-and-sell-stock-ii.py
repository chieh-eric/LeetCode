class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # stack [1]
        # profit 0

        profit = 0
        cur_val = prices[0]

        for price in prices:
            if price > cur_val:
                profit += (price - cur_val)
            cur_val = price
        return profit