class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0]*n
        index = n - 1
        left = 0
        right = n - 1
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2

            if left_square > right_square:
                res[index] = left_square
                left += 1
                index -= 1
            else:
                res[index] = right_square
                right -= 1
                index -= 1
        return res