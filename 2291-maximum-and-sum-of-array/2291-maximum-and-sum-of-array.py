class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        n = len(nums)
        memo = {}

        def dp(i,mask):
            if (i,mask) in memo:
                return memo[(i,mask)]
            
            if i == n:
                return 0

            res = 0
            for slot in range(1,numSlots+1):
                b = 3**(slot-1)
                if mask // b % 3 > 0:
                    res = max(res, (nums[i] & slot) + dp(i+1,mask-b))
            memo[(i,mask)] = res
            return res


        return dp (0,3**numSlots - 1)
