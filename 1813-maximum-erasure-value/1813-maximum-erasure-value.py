class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        n = len(nums)
        contain = set()
        max_val = 0
        cur = 0
        for right in range(n):
            
            while nums[right] in contain:
                contain.remove(nums[left])
                cur -= nums[left]
                left += 1

            contain.add(nums[right])
            cur += nums[right]
            #print(cur)
            max_val = max(max_val, cur)
        return max_val