class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        normal = []
        earn = []
        n = len(transactions)

        for t in transactions:
            if t[1] > t[0]:
                earn.append(t)
            else:
                normal.append(t)
        normal.sort(key=lambda x:x[1])
        earn.sort(key = lambda x:-x[0])
      
        transactions = normal + earn
        val = [v[0] for v in transactions]
        
        left = 0
        right = sum(val)
       # print(transactions)
        while left < right:
            good = True
            mid = (left+right) // 2
            cur = mid
            for i in range(n):
                if cur >= transactions[i][0]:
                    cur = cur - transactions[i][0] +transactions[i][1]
                else:
                    good = False
                    break
            if not good:
               
                left = mid + 1
            else:
                right = mid
        return left