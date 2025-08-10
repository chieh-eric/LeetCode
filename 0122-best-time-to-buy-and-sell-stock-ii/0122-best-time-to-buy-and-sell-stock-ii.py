class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = []
        profit = 0
        for p in prices:
            
            while stack and stack[-1] > p:
                stack.pop()
            
            if stack:
                buy = stack.pop()
                profit += p - buy
            stack.append(p)
        return profit