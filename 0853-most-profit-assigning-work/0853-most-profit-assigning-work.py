class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        n = len(worker)
        total = 0
        m = len(difficulty)
        combine = []
        for i in range(m):
            combine.append((difficulty[i],profit[i]))
        combine.sort(key=lambda x:(x[0],x[1]))

        cur_profit = 0
        for i in range(m):
            cur_profit = max(cur_profit,combine[i][1])
            combine[i] = (combine[i][0],cur_profit)

        def search(val):
            left = 0
            right = len(combine) - 1

            while left < right:
                mid = (left+right+1) // 2
                if combine[mid][0] > val:
                    right = mid - 1
                else:
                    left = mid
            return left


        for i in range(n):
            index = search(worker[i])
            if index == 0 and combine[index][0] > worker[i]:
                continue
            
            total += combine[index][1]
        return total