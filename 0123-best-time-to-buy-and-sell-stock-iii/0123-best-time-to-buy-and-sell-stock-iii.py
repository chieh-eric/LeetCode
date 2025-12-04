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

        stack_prev = []
        max_prift_prev = 0
        for i, price in enumerate(prices):
            while stack_prev and stack_prev[-1] > price:
                stack_prev.pop()
            stack_prev.append(price)
            if len(stack_prev) > 1:
                max_prift_prev = max(max_prift_prev, stack_prev[-1] - stack_prev[0])
            prev[i] = max_prift_prev
        max_prift_prev = max(max_prift_prev, stack_prev[-1] - stack_prev[0])
        #prev[-1] = max_prift_prev
        #print(prev)


        stack_back = []
        max_prift_back = 0
        for i in range(n-1,-1,-1):
            price = prices[i]
            while stack_back and stack_back[-1] < price:
                stack_back.pop()
            stack_back.append(price)
            if len(stack_back) > 1:
                max_prift_back = max(max_prift_back, stack_back[0] - stack_back[-1])
            back[i] = max_prift_back
        max_prift_back = max(max_prift_back, stack_back[0] - stack_prev[-1])
        #back[0] = max_prift_back
        #print(back)
        ans = 0
        for i in range(n):
            ans = max(ans, prev[i] + back[i])
        return ans