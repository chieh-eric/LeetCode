class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # helper(i,k) => Start from index i, can perform k operation. Retrun the maximum length
        ans = 0
        n = len(nums)
        dp = {}

        def helper(i,k):
            if i >= n or k < 0:
                return 0
            if (i,k) in dp:
                return dp[(i,k)]

            mx = 0
            for j in range(i+1,n):
                if nums[j] == nums[i]:
                    mx = max(mx, helper(j,k))
                else:
                    mx = max(mx,helper(j,k-1))
            dp[(i,k)] = mx + 1
            return mx + 1
        for i in range(n):
            ans = max(ans,helper(i,k))
        return ans
       