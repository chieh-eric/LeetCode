class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        def reverse(left,right):

            while left < right:
                nums[left], nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        