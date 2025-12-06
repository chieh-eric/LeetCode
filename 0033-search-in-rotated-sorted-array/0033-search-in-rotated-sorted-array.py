class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left+right+1) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        return -1

