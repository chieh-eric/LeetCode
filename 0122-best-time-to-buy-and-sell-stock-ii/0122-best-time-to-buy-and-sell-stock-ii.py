class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        smallest = prices[0]
        
        n = len(prices)
        for i in range(1, n):
            if prices[i] > smallest:
                profit += (prices[i] - smallest)
                smallest = prices[i]
            else:
                smallest = prices[i]
        return profit