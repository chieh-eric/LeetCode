class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n):
            target = -nums[i]
            dic = {}
            for j in range(i+1,n):
                val = nums[j]
                if val in dic:
                    temp = [nums[i], target-val, val]
                    #print(i,j)
                    res.add(tuple(temp))
                    continue
                dic[target - val] = j
        #print(res)
        #ans = []
            
        return list(res)
        