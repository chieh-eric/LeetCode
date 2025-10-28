from collections import defaultdict
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Appraoch
        # Use two dictionary
        # 1. Record all previous value
        # 2. Record the difference value

        # value -> End with this value, with value y -> val: maximum length

        n = len(nums)
        value = {}

        for i in range(n):
            if i not in value:
                    value[i] = {}

            for j in range(i):
                diff = nums[j] - nums[i]
                if diff not in value[i]:
                    value[i][diff] = 2

                if diff in value[j]:
                    value[i][diff] = max(value[j][diff]+1, value[i][diff])
                
        #print(value)
        max_val = 0
        for key in value:
            for prev in value[key]:
                max_val = max(max_val, value[key][prev])

        return max_val

        