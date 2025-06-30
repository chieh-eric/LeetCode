from collections import Counter
class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = Counter(nums)
        if count[nums[0]] == 1:
            return 1
        
        for key in count:
            if key != nums[0] and key % nums[0] != 0:
                return 1
        
        return (count[nums[0]]+1)/2
