class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        # 1, 2, 3, 4, 6
        # Apply binary search, SortedList -> Dynamically change
        # arr = [] -> Store possible maximum value
        # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
        # TC(n**2* log(n))
        
        rewardValues.sort()
        maxiumValue = SortedList()
        exist = set()

        for val in rewardValues:
            if not maxiumValue:
                maxiumValue.add(val)
                exist.add(val)
            else:
                idx = maxiumValue.bisect_left(val) - 1
                if val not in exist:
                    maxiumValue.add(val)
                    exist.add(val)
                for i in range(idx+1):
                    if maxiumValue[i] + val not in exist:
                        exist.add(maxiumValue[i] + val)
                        maxiumValue.add(maxiumValue[i] + val)
        #print(maxiumValue)
        return maxiumValue[-1]

