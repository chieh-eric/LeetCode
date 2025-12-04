class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # prev = [], prev[i] -> start from day 0 to day i, max profit
        # back = [], back[i] -> start from day i to end, max profit
        n = len(prices)
        prev = [0]*(n)
        back = [0]*(n)

        max_prift_prev = 0
        left_min = float('inf')
        for i, price in enumerate(prices):
            left_min = min(left_min, price)
            max_prift_prev = max(max_prift_prev, price - left_min)
            prev[i] = max_prift_prev


        max_prift_back = 0
        right_max = 0
        for i in range(n-1,-1,-1):
            price = prices[i]
            right_max = max(price, right_max)
            max_prift_back = max(max_prift_back, right_max - price )
            back[i] = max_prift_back
        #back[0] = max_prift_back
        #print(back)
        ans = 0
        for i in range(n):
            ans = max(ans, prev[i] + back[i])
        return ans