class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profix = 0
        stack = []
        for price in prices:
            while stack and stack[-1] > price:
                stack.pop()
            if stack:
                max_profix = max(max_profix, price - stack[0])
            stack.append(price)
        return max_profix


        