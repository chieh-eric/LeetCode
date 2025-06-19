class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        nums.sort()
        dic = {}
        for num in nums:
            key = num % space
            if key not in dic:
                dic[key] = 0
            dic[key] += 1
        max_val = max(dic.values())
       
        for num in nums:
            if dic[num % space] == max_val:
                return num
