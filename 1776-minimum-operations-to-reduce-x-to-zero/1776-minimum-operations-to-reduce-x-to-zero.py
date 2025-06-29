class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        target = total - x
        if target == 0:
            return n
        dic = {}
        prefix = 0
        max_length = -1
        for i in range(n):
            
            prefix += nums[i]
            if prefix == target:
                max_length = max(max_length,i+1)
            elif (prefix - target) in dic:
                max_length = max(max_length, i-dic[prefix - target])
            dic[prefix] = i
        return n - max_length if max_length != -1 else -1