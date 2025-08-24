class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        arr = SortedList()
        for num in nums:
            if num not in dic:
                dic[num] = True
                arr.add(num)
        return arr[-3] if len(arr) > 2 else arr[-1]


        