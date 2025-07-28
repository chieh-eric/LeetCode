class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        n = len(nums)
  
        
        count = 0
        bad_pos = min_pos = max_pos = -1
        for right, val in enumerate(nums):
            if val > maxK or val < minK:
                bad_pos = right
                
            if val == minK:
                min_pos = right
                
            if val == maxK:
                max_pos = right
                
            min_index = min(min_pos,max_pos)
            if min_index > bad_pos:
                count += (min_index-bad_pos)
        return count

