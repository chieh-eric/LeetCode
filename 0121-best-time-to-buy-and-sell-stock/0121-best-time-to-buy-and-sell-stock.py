class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10001
        profit = 0
        for i in range(len(prices)):
            if(buy > prices[i]):
                buy = prices[i]
            if(profit < prices[i] - buy):
                profit = prices[i] - buy
        return profit