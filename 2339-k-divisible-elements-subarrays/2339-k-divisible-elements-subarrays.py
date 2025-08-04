class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        valid = {}
        n = len(nums)
        counts = [0]*n
        for i,num in enumerate(nums):
            if num % p == 0:
                counts[i] = 1

        for right in range(1,n+1):
            left = right - 1
            count = 0
            while left >= 0:
                count += counts[left]
                if count > k:
                    break
                valid[tuple(nums[left:right])] = True
                left -= 1
        return len(valid)
