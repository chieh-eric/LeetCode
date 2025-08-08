class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        arr = nums[-k:] + nums[:-k]
        #print(arr)
        for i in range(len(nums)):
            nums[i] = arr[i]
        