class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        loss = 0
        max_val = 0
        for t in transactions:
            loss += max(0,t[0]-t[1])
            max_val = max(max_val,min(t[0],t[1]))
        return loss + max_val
        # x - 8 - 9 + 3 - 3 + 3 - 7 + 4 - 7