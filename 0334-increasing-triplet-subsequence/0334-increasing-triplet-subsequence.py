import bisect
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = []
        for val in nums:
            idx = bisect.bisect_left(arr, val)
            if idx == len(arr):
                arr.append(val)
            else:
                arr[idx] = val

            if len(arr) >= 3:
                return True

        return False

            