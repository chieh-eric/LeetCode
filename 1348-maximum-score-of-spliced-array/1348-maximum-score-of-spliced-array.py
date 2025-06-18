class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
       
        dp = [0]*n
        dp[0] = nums1[0] - nums2[0]
        for i in range(1,n):
            diff = nums1[i] - nums2[i]
            dp[i] = max(dp[i-1]+diff,diff)

        dp1 = [0]*n
        dp1[0] = nums2[0] - nums1[0]
        for i in range(1,n):
            diff = nums2[i] - nums1[i]
            dp1[i] = max(dp1[i-1]+diff,diff)
        
        return max(max(dp)+sum(nums2),max(dp1)+sum(nums1))
       