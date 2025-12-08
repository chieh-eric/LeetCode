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
        rest = [0]*n
        hold = [0]*n
        sold = [0]*n
        hold[0] = -prices[0]

        for i in range(1, n):
            rest[i] = max(rest[i-1], sold[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
        # print(rest)
        # print(hold)
        # print(sold)
        return max(rest[n-1], sold[n-1])

