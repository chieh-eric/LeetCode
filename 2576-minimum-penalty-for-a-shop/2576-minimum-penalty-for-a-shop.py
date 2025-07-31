class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
        suffix = [0]*(n+1)

        cur = 0
        for i in range(n-1,-1,-1):
            if customers[i] == "Y":
                cur += 1
            suffix[i] = cur
        
        min_val = float('inf')
        early_index = -1
        cur = 0
        for i in range(n+1):
            if min_val > cur + suffix[i]:
                min_val = cur + suffix[i]
                early_index = i
            if i < n and customers[i] == "N":
                cur += 1
        return early_index