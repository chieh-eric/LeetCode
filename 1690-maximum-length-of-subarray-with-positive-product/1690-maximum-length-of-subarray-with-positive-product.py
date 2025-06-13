class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate the prfix, treat 0 as special case
        # -1 -2 -3 4 5
        n = len(nums)
        negative = [0] * n
        positive = [0] * n

        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:
            negative[0] = 1

        for i in range(1,n):
            num = nums[i]
            if num == 0:
                continue
            if num > 0:
                
                positive[i] = max(1,positive[i-1] + 1)
                if negative[i-1]:
                    negative[i] = negative[i-1] + 1
            else:
                if negative[i-1]:
                    positive[i] = negative[i-1] + 1
                negative[i] = positive[i-1] + 1
      
        return max(positive)