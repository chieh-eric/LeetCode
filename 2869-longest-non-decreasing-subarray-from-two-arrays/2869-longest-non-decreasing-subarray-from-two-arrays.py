from collections import defaultdict
class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j] -> index, j -> dictionary 2 value; the maximum subarray which end in this index and value
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        # Initial case
        dp[0][nums1[0]] = 1
        dp[0][nums2[0]] = 1
        #print(dp)

        max_len = 1
        for i in range(1, n):
            num1 = nums1[i]
            num2 = nums2[i]
            for val in dp[i-1]:
                if num1 >= val:
                    dp[i][num1] = max(dp[i][num1], dp[i-1][val])
                
                if num2 >= val:
                    dp[i][num2] = max(dp[i][num2], dp[i-1][val])
            if num1 != num2:
                dp[i][num1] += 1
                dp[i][num2] += 1
            else:
                dp[i][num1] += 1
            max_len = max(max_len, dp[i][num1], dp[i][num2])
        #print(dp)
        
        return max_len 



        