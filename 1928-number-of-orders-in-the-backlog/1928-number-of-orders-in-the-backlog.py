import heapq
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        buy = []
        sell = []
        mod = 10**9 + 7
        for price, num, t in orders:
            # if type is buy
            if t == 0:
                current_sell = sell[0][0] if sell else 0
                while sell and  current_sell <= price and num:
                    val = min(num,sell[0][1])
                    num -= val
                    sell[0] = (sell[0][0],sell[0][1] - val)
                    if sell[0][1] == 0:
                        heapq.heappop(sell)

                    if num == 0:
                        continue
                    current_sell = sell[0][-0] if sell else 0
                if num > 0:
                    heapq.heappush(buy,(-price,num))
            else:
                current_buy = -buy[0][0] if buy else 0
                while buy and  current_buy >= price and num:
                    val = min(num,buy[0][1])
                    num -= val
                    buy[0] = (buy[0][0],buy[0][1] - val)
                    if buy[0][1] == 0:
                        heapq.heappop(buy)

                    if num == 0:
                        continue
                    current_buy = -buy[0][0] if buy else 0
                if num > 0:
                    heapq.heappush(sell,(price,num))
         
        count = 0
        for _,num in buy:
            count += num
        for _,num in sell:
            count += num
        return count % mod
                        