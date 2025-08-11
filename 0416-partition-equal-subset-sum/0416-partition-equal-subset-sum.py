class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        
        dic = {0:True}
        for num in nums:
            if target in dic:
                return True
            temp = dic.copy()
            for key in temp:
                dic[key+num] = True
        return False