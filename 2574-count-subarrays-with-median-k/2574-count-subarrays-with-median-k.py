from collections import Counter
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = Counter()
        balance = 0
        count[0] = 1
        idx = nums.index(k)

        res = 0
        for i in range(idx-1,-1,-1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            count[balance] += 1
            
        balance = 0
        for i in range(idx,n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

            res += count[-balance] + count[-balance+1]
        return res