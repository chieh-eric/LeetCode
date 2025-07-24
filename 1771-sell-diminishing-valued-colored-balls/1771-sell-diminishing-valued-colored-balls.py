import bisect
class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        mod = 10**9 + 7
        def calculate(start,end):
            return (start+end)*(start-end+1) // 2

        res = SortedList()
        for item in inventory:
            res.add(item)

        count = 0
        n = len(res)
        while orders > 0:
            largest = res[-1]
            second_large = bisect.bisect_left(res,largest) - 1
            second_value = res[second_large] if second_large != -1 else 0
            batch = (n-second_large-1)
            # print("start")
            # print(largest)
            # print(second_large)
            # print(second_value)
            # print(batch)
           

            difference = largest - second_value

            
            if orders >= difference*batch:
                ans = calculate(largest,second_value+1)
                count += ans*batch % mod
                orders -= difference*batch
                del res[second_large:]
                res.update([second_value]*batch)
                
            else:
                avg = orders // batch
                remain = orders % batch
                #print(res)
                #print(avg)
                #print(remain)
                ans = calculate(largest, largest-avg+1)
                #print(ans)
                count += ans*batch % mod
                count += (largest-avg)*remain % mod
                orders = 0
            #print(count)
        return count % mod
