import bisect
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
      
        nums.sort()
        count = 0
        for i in range(n):
            l = lower - nums[i]
            u = upper - nums[i]
            low_index = bisect.bisect_left(nums,l,i+1,n)
            up_index = bisect.bisect_right(nums,u,i+1,n)
            count += (up_index-low_index)
        return count
