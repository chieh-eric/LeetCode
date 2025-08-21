class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        n = len(nums)

        count = 0
        max_len = 0
        for right in range(n):
            if nums[right] == 0:
                count += 1
            
            while count > k :
                if nums[left] == 0:
                    count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            #print(max_len)
        return max_len