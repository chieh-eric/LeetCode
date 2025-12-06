class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first_min = float("inf")
        second_min = float('inf')
        for val in nums:
            if first_min >= val:
                first_min = val
            elif second_min >= val:
                second_min = val
            else:
                return True

        return False
       

            