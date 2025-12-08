class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Three state
        # 1. Cool down
        # rest[i] = max(res[i-1], sold[i-1])
        # 2. having stcok can sall
        # hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        # 3. sell stock
        # sold[i] = price[i] + hold[i-1]
        n = len(prices)
        rest = hold = sold = 0
        hold = -prices[0]
        for i in range(n):
            hold = max(hold, rest - prices[i])
            rest = max(rest, sold)
            sold = hold + prices[i]
        return max(rest, sold)

