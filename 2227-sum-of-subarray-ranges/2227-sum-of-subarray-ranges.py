class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        min_val = [[float('inf')]*n for _ in range(n)]
        max_val = [[-float('inf')]*n for _ in range(n)]

        for i in range(n):
            min_val[i][i] = max_val[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                max_val[i][j] = max(max_val[i][j-1], nums[j])
                min_val[i][j] = min(min_val[i][j-1], nums[j])
        #print(max_val)
        #print(min_val)
        for i in range(n):
            for j in range(n):
                if  max_val[i][j] != -float('inf'):
                    total += max_val[i][j] - min_val[i][j]
        return total