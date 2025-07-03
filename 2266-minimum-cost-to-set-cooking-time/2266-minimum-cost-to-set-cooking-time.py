class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        def calculate(s,pos):
            i = 0
            n = len(s)
            cur_pos = pos
            cost = 0
            while i < n:
                    
                if cur_pos != s[i]:
                    cur_pos = s[i]
                    cost += moveCost

                if cur_pos == s[i]:
                    cost += pushCost
                i += 1
            return cost
        res = []
        cost = float('inf')
        if targetSeconds < 60:
            res = [int(val) for val in str(targetSeconds)]
            cost = min(cost,calculate(res,startAt))
        else:
            minute1 = str(targetSeconds // 60)
            
            second1 = str(targetSeconds % 60) if targetSeconds % 60 >= 10 else "0" + str(targetSeconds % 60)
            if len(minute1) < 3:
                res = [int(val) for val in minute1 + second1]
                #print(res)
                cost = min(cost,calculate(res,startAt))
            if int(second1) <= 39:
                minute2 = str(int(minute1)-1) if int(minute1) - 1 > 0 else ""
                second2 = str(int(second1)+60)
                res = [int(val) for val in minute2 + second2]
                #print(res)
                cost = min(cost,calculate(res,startAt))
                

        return cost
                