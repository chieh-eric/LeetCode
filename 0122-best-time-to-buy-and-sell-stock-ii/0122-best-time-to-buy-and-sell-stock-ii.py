class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # stack [1]
        # profit 0

        profit = 0
        stack = []

        for price in prices:
            if stack:
                if stack[-1] > price:
                    if len(stack) > 1:
                        profit += (stack[-1] - stack[0])
                    stack = []
            stack.append(price)
        
        if len(stack) > 1:
            profit += (stack[-1] - stack[0])

        return profit