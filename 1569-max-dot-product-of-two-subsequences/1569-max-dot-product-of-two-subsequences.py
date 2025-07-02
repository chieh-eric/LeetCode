class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j] means the maximum dot product of two subsequence when raech in pos i in nums1 and pos j in nums2
        n = len(nums1)
        m = len(nums2)

        dp = [[-float('inf')]*m for _ in range(n)]
        dp[0][0] = nums1[0]*nums2[0]
        for j in range(1,m):
            dp[0][j] = max(dp[0][j-1],nums1[0]*nums2[j])
        
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], nums2[0]*nums1[i])
        
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], nums1[i]*nums2[j], dp[i-1][j-1]+nums1[i]*nums2[j])
        return dp[-1][-1]
        
        # 6 6 6
        # 6 6 6
        # 6 
        # 15