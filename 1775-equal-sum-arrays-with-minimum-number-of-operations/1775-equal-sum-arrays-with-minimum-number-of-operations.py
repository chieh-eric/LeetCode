class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Use two sortedList
        # Calculate sum of two list
        # sumNums1 -> 7
        # SortedNums1 = [1,6]
        # sumNums2 -> 2
        # SortedNums2 = [2]
        # while diff > 0:

        sumNums1 = sumNums2 = 0
        sortNums1 = SortedList()
        sortNums2 = SortedList()

        for val in nums1:
            sumNums1 += val
            sortNums1.add(val)
        
        for val in nums2:
            sumNums2 += val
            sortNums2.add(val)
        
        operation = 0
        if sumNums1 < sumNums2:
            sortNums1, sortNums2 = sortNums2, sortNums1
            sumNums1, sumNums2 = sumNums2, sumNums1
        
        diff = sumNums1 - sumNums2

        while diff > 0:
            operation += 1
            delta_decrease = min(sortNums1[-1] - 1, diff)
            delta_increase = min(6 - sortNums2[0], diff)
            if delta_decrease == delta_increase and delta_increase == 0:
                return -1

            if delta_decrease >= delta_increase:
                diff -= delta_decrease
                sortNums1.add(sortNums1[-1] - delta_decrease)
                sortNums1.pop()
            else:
                diff -= delta_increase
                sortNums2.add(sortNums2[0] + delta_increase)
                sortNums2.pop(0)
        return operation



        
